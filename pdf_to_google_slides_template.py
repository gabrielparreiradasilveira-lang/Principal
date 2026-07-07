#!/usr/bin/env python3
"""
PDF to Google Slides com Template Clone
Clona seu template Google Slides e preenche com conteúdo do PDF
"""

import os
import json
from typing import List, Dict
from PyPDF2 import PdfReader
import shutil

try:
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload
except ImportError:
    print("Instalando Google APIs...")
    os.system("pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from googleapiclient.discovery import build
    from googleapiclient.http import MediaFileUpload


class PDFToGoogleSlidesTemplate:
    # ID do seu template - ALTERE AQUI!
    TEMPLATE_ID = "1_M9kVI00iLgRO1IHITh5LWAuH48febps-tSUjEZ9V90"

    def __init__(self, pdf_path: str, credentials_json: str = None, drive_folder_id: str = None):
        """
        Args:
            pdf_path: Caminho para o PDF
            credentials_json: Caminho para arquivo de credenciais JSON
            drive_folder_id: ID da pasta do Google Drive (opcional)
        """
        self.pdf_path = pdf_path
        self.credentials_json = credentials_json
        self.drive_folder_id = drive_folder_id
        self.slides_service = None
        self.drive_service = None

        if credentials_json and os.path.exists(credentials_json):
            self._authenticate()

    def _authenticate(self):
        """Autentica com Google APIs"""
        try:
            creds = Credentials.from_service_account_file(
                self.credentials_json,
                scopes=[
                    'https://www.googleapis.com/auth/presentations',
                    'https://www.googleapis.com/auth/drive'
                ]
            )
            self.slides_service = build('slides', 'v1', credentials=creds)
            self.drive_service = build('drive', 'v3', credentials=creds)
            print("✅ Autenticado com Google APIs")
        except Exception as e:
            print(f"❌ Erro na autenticação: {e}")
            return False
        return True

    def extract_text_from_pdf(self) -> List[Dict]:
        """Extrai texto estruturado do PDF"""
        print(f"📄 Extraindo conteúdo de {os.path.basename(self.pdf_path)}...")
        pages_content = []

        try:
            pdf_reader = PdfReader(self.pdf_path)
            total_pages = len(pdf_reader.pages)

            for page_num, page in enumerate(pdf_reader.pages, 1):
                text = page.extract_text()

                if text and text.strip():
                    lines = [line.strip() for line in text.split('\n') if line.strip()]

                    pages_content.append({
                        'page_num': page_num,
                        'total_pages': total_pages,
                        'title': lines[0][:80] if lines else f"Página {page_num}",
                        'content': '\n'.join(lines[1:]) if len(lines) > 1 else text,
                        'full_text': text
                    })

            print(f"✅ {len(pages_content)} páginas extraídas")
            return pages_content
        except Exception as e:
            print(f"❌ Erro ao extrair PDF: {e}")
            return []

    def copy_template(self, new_title: str) -> str:
        """Clona o template para novo arquivo"""
        if not self.slides_service:
            print("❌ Erro: Não autenticado")
            return None

        try:
            # Copia o template
            copy_request_body = {
                'name': new_title
            }

            copied_file = self.drive_service.files().copy(
                fileId=self.TEMPLATE_ID,
                body=copy_request_body
            ).execute()

            presentation_id = copied_file.get('id')
            print(f"✅ Template clonado: {new_title}")

            # Move para pasta se especificado
            if self.drive_folder_id:
                self.drive_service.files().update(
                    fileId=presentation_id,
                    addParents=self.drive_folder_id,
                    removeParents='root'
                ).execute()
                print(f"✅ Arquivo salvo na pasta especificada")

            return presentation_id
        except Exception as e:
            print(f"❌ Erro ao clonar template: {e}")
            return None

    def get_presentation_layout(self, presentation_id: str) -> Dict:
        """Obtém informações do layout do template"""
        try:
            presentation = self.slides_service.presentations().get(
                presentationId=presentation_id
            ).execute()

            slides = presentation.get('slides', [])
            print(f"📊 Template tem {len(slides)} slides")

            layout_info = {
                'total_slides': len(slides),
                'slides': []
            }

            for idx, slide in enumerate(slides[:3]):  # Primeiros 3 slides
                shapes = slide.get('pageElements', [])
                layout_info['slides'].append({
                    'index': idx,
                    'shapes_count': len(shapes),
                    'shapes': []
                })

                for shape in shapes:
                    if 'textBox' in shape:
                        text = shape['textBox'].get('textElements', [])
                        layout_info['slides'][idx]['shapes'].append({
                            'type': 'textBox',
                            'text_count': len(text)
                        })

            return layout_info
        except Exception as e:
            print(f"⚠️  Não consegui analisar o template: {e}")
            return {}

    def fill_template_with_content(self, presentation_id: str, pages_content: List[Dict]):
        """Preenche template com conteúdo do PDF"""
        if not self.slides_service:
            print("❌ Erro: Não autenticado")
            return False

        try:
            # Obtém apresentação atual
            presentation = self.slides_service.presentations().get(
                presentationId=presentation_id
            ).execute()

            slides = presentation.get('slides', [])
            print(f"📝 Preenchendo {len(pages_content)} páginas...")

            requests = []

            # Para cada página do PDF
            for page_idx, page_data in enumerate(pages_content):
                # Usa slides existentes ou cria novos
                if page_idx < len(slides):
                    # Usa slide existente
                    slide_id = slides[page_idx].get('objectId')
                else:
                    # Cria novo slide baseado no template
                    slide_id = f'slide_{page_idx}'
                    requests.append({
                        'addSlide': {
                            'objectId': slide_id,
                            'slideLayout': {
                                'predefinedLayout': 'TITLE_AND_BODY'
                            }
                        }
                    })

                # Atualiza título (primeiro elemento de texto encontrado)
                title_request = {
                    'updateTextContent': {
                        'objectId': f'{slide_id}#title',
                        'textContent': {
                            'text': page_data['title']
                        }
                    }
                }

                # Atualiza conteúdo
                content_request = {
                    'updateTextContent': {
                        'objectId': f'{slide_id}#body',
                        'textContent': {
                            'text': page_data['content']
                        }
                    }
                }

                requests.append(title_request)
                requests.append(content_request)

            # Executa todas as mudanças
            if requests:
                self.slides_service.presentations().batchUpdate(
                    presentationId=presentation_id,
                    body={'requests': requests}
                ).execute()

            print(f"✅ Conteúdo preenchido com sucesso!")
            return True
        except Exception as e:
            print(f"❌ Erro ao preencher template: {e}")
            return False

    def convert(self, output_folder: str = None) -> str:
        """Executa conversão completa"""
        if not self.slides_service:
            print("❌ Erro: Configure credenciais do Google primeiro!")
            print("\n📋 Setup necessário:")
            print("1. Vá para https://console.cloud.google.com")
            print("2. Crie um novo projeto")
            print("3. Ative Google Slides API e Google Drive API")
            print("4. Crie uma Service Account")
            print("5. Baixe JSON e salve como 'credentials.json'")
            print("6. Execute novamente com: python pdf_to_google_slides_template.py <pdf> credentials.json")
            return None

        # Extrai conteúdo do PDF
        pages_content = self.extract_text_from_pdf()
        if not pages_content:
            return None

        # Nome do novo arquivo
        pdf_name = os.path.basename(self.pdf_path).replace('.pdf', '')
        new_title = f"{pdf_name} - Convertido"

        # Clona template
        presentation_id = self.copy_template(new_title)
        if not presentation_id:
            return None

        # Preenche com conteúdo
        if self.fill_template_with_content(presentation_id, pages_content):
            # Retorna URL
            url = f"https://docs.google.com/presentation/d/{presentation_id}/edit"
            print(f"\n🎉 Pronto! Acesse aqui:")
            print(f"🔗 {url}")
            return url
        else:
            return None


def main():
    import sys

    print("""
    ╔════════════════════════════════════════════════════════════╗
    ║  PDF to Google Slides com Seu Template                    ║
    ║  Clona seu template e preenche com conteúdo do PDF       ║
    ╚════════════════════════════════════════════════════════════╝
    """)

    if len(sys.argv) < 2:
        print("Uso:")
        print("  python pdf_to_google_slides_template.py <arquivo.pdf> [credentials.json] [folder_id]")
        print("\nExemplo:")
        print("  python pdf_to_google_slides_template.py documento.pdf credentials.json")
        print("\nSe não tiver credentials.json:")
        print("  1. Vá para https://console.cloud.google.com")
        print("  2. Crie projeto e Service Account")
        print("  3. Baixe JSON com as credenciais")
        sys.exit(1)

    pdf_path = sys.argv[1]
    credentials_json = sys.argv[2] if len(sys.argv) > 2 else None
    folder_id = sys.argv[3] if len(sys.argv) > 3 else None

    if not os.path.exists(pdf_path):
        print(f"❌ Arquivo não encontrado: {pdf_path}")
        sys.exit(1)

    converter = PDFToGoogleSlidesTemplate(pdf_path, credentials_json, folder_id)
    converter.convert()


if __name__ == "__main__":
    main()
