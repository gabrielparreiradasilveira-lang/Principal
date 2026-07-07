#!/usr/bin/env python3
"""
PDF to Google Slides Converter
Cria apresentação diretamente no Google Slides
"""

import os
import json
from typing import List
from PyPDF2 import PdfReader

try:
    from google.auth.transport.requests import Request
    from google.oauth2.service_account import Credentials
    from google.oauth2 import service_account
    from googleapiclient.discovery import build
except ImportError:
    print("Para usar Google Slides, instale:")
    print("pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client")


class PDFToGoogleSlidesConverter:
    def __init__(self, pdf_path: str, credentials_json: str = None):
        self.pdf_path = pdf_path
        self.credentials_json = credentials_json
        self.slides_service = None

        if credentials_json:
            self._authenticate()

    def _authenticate(self):
        """Autentica com Google Slides API"""
        creds = service_account.Credentials.from_service_account_file(
            self.credentials_json,
            scopes=['https://www.googleapis.com/auth/presentations']
        )
        self.slides_service = build('slides', 'v1', credentials=creds)

    def extract_text_from_pdf(self) -> List[dict]:
        """Extrai texto do PDF"""
        pages_content = []
        pdf_reader = PdfReader(self.pdf_path)

        for page_num, page in enumerate(pdf_reader.pages, 1):
            text = page.extract_text()
            pages_content.append({
                'page_num': page_num,
                'text': text
            })

        return pages_content

    def create_presentation(self) -> str:
        """Cria apresentação no Google Slides"""
        if not self.slides_service:
            print("❌ Erro: Não autenticado com Google Slides")
            return None

        # Nome da apresentação
        pdf_name = os.path.basename(self.pdf_path).replace('.pdf', '')
        presentation_body = {
            'title': f'{pdf_name} - Convertido de PDF'
        }

        # Cria apresentação
        presentation = self.slides_service.presentations().create(
            body=presentation_body
        ).execute()

        presentation_id = presentation.get('presentationId')
        print(f"✅ Apresentação criada: {presentation_id}")

        # Extrai conteúdo do PDF
        pages_content = self.extract_text_from_pdf()

        # Adiciona slides
        requests = []
        for page_data in pages_content:
            text = page_data['text']
            if text and text.strip():
                lines = text.split('\n')
                title = lines[0][:60] if lines else "Página"
                content = '\n'.join(lines[1:]) if len(lines) > 1 else text

                # Cria novo slide
                requests.append({
                    'addSlide': {
                        'objectId': f'slide_{page_data["page_num"]}',
                        'slideLayout': {
                            'predefinedLayout': 'TITLE_AND_BODY'
                        }
                    }
                })

                # Adiciona título
                requests.append({
                    'updateTextContent': {
                        'objectId': f'slide_{page_data["page_num"]}#title',
                        'textContent': {
                            'text': title
                        }
                    }
                })

                # Adiciona conteúdo
                requests.append({
                    'updateTextContent': {
                        'objectId': f'slide_{page_data["page_num"]}#body',
                        'textContent': {
                            'text': content
                        }
                    }
                })

        # Executa todas as mudanças
        if requests:
            self.slides_service.presentations().batchUpdate(
                presentationId=presentation_id,
                body={'requests': requests}
            ).execute()

        return presentation_id


def main():
    print("""
    ╔════════════════════════════════════════════╗
    ║  PDF to Google Slides Converter            ║
    ║  Converta PDFs em apresentações Google     ║
    ╚════════════════════════════════════════════╝
    """)

    print("⚠️  Para usar com Google Slides, você precisa:")
    print("1. Criar um projeto no Google Cloud Console")
    print("2. Habilitar Google Slides API")
    print("3. Criar uma Service Account e baixar JSON")
    print("4. Executar: python pdf_to_google_slides.py <pdf> <credentials.json>")
    print("\nAlternativa: Use o script pdf_to_slides.py para gerar PPTX!")


if __name__ == "__main__":
    main()
