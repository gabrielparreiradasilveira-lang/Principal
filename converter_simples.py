#!/usr/bin/env python3
"""
PDF to Google Slides - Versão Simples (Sem Google Cloud Console)
Autentica uma única vez, depois é automático!
"""

import os
import pickle
from pathlib import Path
from typing import List, Dict
from PyPDF2 import PdfReader
import webbrowser

try:
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from google.oauth2 import service_account
    from google.auth.oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build
except ImportError:
    print("Instalando dependências...")
    os.system("pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client PyPDF2")
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from google.oauth2 import service_account
    from google.auth.oauthlib.flow import InstalledAppFlow
    from googleapiclient.discovery import build


class ConversorPDFSimples:
    """
    Conversor de PDF para Google Slides com autenticação simples
    """

    # ID do seu template (substitua com seu próprio se desejar)
    TEMPLATE_ID = "1_M9kVI00iLgRO1IHITh5LWAuH48febps-tSUjEZ9V90"

    # Arquivo onde salva o token (não remova!)
    TOKEN_FILE = "token.pickle"

    # Escopos necessários
    SCOPES = [
        'https://www.googleapis.com/auth/presentations',
        'https://www.googleapis.com/auth/drive'
    ]

    def __init__(self):
        self.slides_service = None
        self.drive_service = None
        self._autenticar()

    def _autenticar(self):
        """
        Autentica com Google (primeira vez abre navegador, depois usa token salvo)
        """
        creds = None

        # Tenta carregar token salvo
        if os.path.exists(self.TOKEN_FILE):
            with open(self.TOKEN_FILE, 'rb') as token:
                creds = pickle.load(token)
                print("✅ Token carregado - Autenticado!")

        # Se não tem token ou expirou, faz autenticação nova
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                print("🔄 Atualizando credenciais...")
                creds.refresh(Request())
            else:
                print("\n🔐 Primeira vez? Vou abrir o navegador para você autorizar...")
                print("   (Isso só acontece uma vez!)\n")

                # Cria flow de autenticação
                flow = InstalledAppFlow.from_client_secrets_file(
                    'credentials_oauth.json',
                    self.SCOPES
                )

                # Abre navegador
                creds = flow.run_local_server(port=0)

            # Salva token para próximas vezes
            with open(self.TOKEN_FILE, 'wb') as token:
                pickle.dump(creds, token)
                print("✅ Token salvo! Próximas vezes será automático.\n")

        # Cria serviços
        self.slides_service = build('slides', 'v1', credentials=creds)
        self.drive_service = build('drive', 'v3', credentials=creds)

    def extrair_pdf(self, caminho_pdf: str) -> List[Dict]:
        """Extrai conteúdo do PDF"""
        print(f"📄 Extraindo: {os.path.basename(caminho_pdf)}...")

        paginas = []
        pdf_reader = PdfReader(caminho_pdf)

        for num_pagina, pagina in enumerate(pdf_reader.pages, 1):
            texto = pagina.extract_text()

            if texto and texto.strip():
                linhas = [l.strip() for l in texto.split('\n') if l.strip()]

                paginas.append({
                    'numero': num_pagina,
                    'titulo': linhas[0][:80] if linhas else f"Página {num_pagina}",
                    'conteudo': '\n'.join(linhas[1:]) if len(linhas) > 1 else texto,
                })

        print(f"✅ {len(paginas)} páginas extraídas\n")
        return paginas

    def clonar_template(self, novo_titulo: str) -> str:
        """Clona seu template do Google Slides"""
        print(f"📋 Clonando template...")

        try:
            corpo = {'name': novo_titulo}

            arquivo_clonado = self.drive_service.files().copy(
                fileId=self.TEMPLATE_ID,
                body=corpo
            ).execute()

            id_apresentacao = arquivo_clonado.get('id')
            print(f"✅ Template clonado!\n")

            return id_apresentacao
        except Exception as e:
            print(f"❌ Erro ao clonar template: {e}")
            return None

    def preencher_slides(self, id_apresentacao: str, paginas: List[Dict]) -> bool:
        """Preenche os slides com conteúdo do PDF"""
        print(f"✍️  Preenchendo {len(paginas)} slides...\n")

        try:
            requisicoes = []

            for idx, pagina in enumerate(paginas):
                # ID único para cada slide
                id_slide = f'slide_{idx}'

                # Cria novo slide
                requisicoes.append({
                    'addSlide': {
                        'objectId': id_slide,
                        'slideLayout': {
                            'predefinedLayout': 'TITLE_AND_BODY'
                        }
                    }
                })

                # Adiciona título
                requisicoes.append({
                    'updateTextContent': {
                        'objectId': f'{id_slide}#title',
                        'textContent': {
                            'text': pagina['titulo']
                        }
                    }
                })

                # Adiciona conteúdo
                requisicoes.append({
                    'updateTextContent': {
                        'objectId': f'{id_slide}#body',
                        'textContent': {
                            'text': pagina['conteudo']
                        }
                    }
                })

            # Executa todas as mudanças
            self.slides_service.presentations().batchUpdate(
                presentationId=id_apresentacao,
                body={'requests': requisicoes}
            ).execute()

            print(f"✅ Slides preenchidos!\n")
            return True
        except Exception as e:
            print(f"❌ Erro ao preencher: {e}")
            return False

    def converter(self, caminho_pdf: str) -> str:
        """Executa conversão completa"""
        print("=" * 60)
        print("  PDF → Google Slides")
        print("=" * 60 + "\n")

        if not os.path.exists(caminho_pdf):
            print(f"❌ Arquivo não encontrado: {caminho_pdf}")
            return None

        # Extrai conteúdo
        paginas = self.extrair_pdf(caminho_pdf)
        if not paginas:
            return None

        # Nome novo
        nome_arquivo = Path(caminho_pdf).stem
        novo_titulo = f"{nome_arquivo} - Convertido"

        # Clona template
        id_apresentacao = self.clonar_template(novo_titulo)
        if not id_apresentacao:
            return None

        # Preenche com conteúdo
        if self.preencher_slides(id_apresentacao, paginas):
            url = f"https://docs.google.com/presentation/d/{id_apresentacao}/edit"

            print("=" * 60)
            print("🎉 PRONTO! Seu slide foi criado no Google Drive!")
            print("=" * 60)
            print(f"\n🔗 Abra aqui:")
            print(f"   {url}\n")

            return url

        return None


def main():
    import sys

    if len(sys.argv) < 2:
        print("""
╔════════════════════════════════════════════════════════════╗
║         PDF → Google Slides (Versão Simples)              ║
║     Autentica uma vez, depois é automático!               ║
╚════════════════════════════════════════════════════════════╝

Uso:
  python converter_simples.py seu_documento.pdf

Exemplo:
  python converter_simples.py aula1.pdf
  python converter_simples.py aula2.pdf

Primeira vez:
  • Abre o navegador
  • Você autoriza
  • Pronto! Token salvo

Próximas vezes:
  • Automático (sem autorização)
  • Só rodar o comando!
        """)
        sys.exit(1)

    caminho_pdf = sys.argv[1]

    conversor = ConversorPDFSimples()
    conversor.converter(caminho_pdf)


if __name__ == "__main__":
    main()
