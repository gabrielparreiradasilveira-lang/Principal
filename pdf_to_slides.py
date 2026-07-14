#!/usr/bin/env python3
"""
PDF to Google Slides Converter
Extrai conteúdo de PDF e cria apresentação no Google Slides
"""

import os
import sys
from pathlib import Path
from typing import List, Tuple
import json

try:
    from PyPDF2 import PdfReader
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.enum.text import PP_ALIGN
    from pptx.dml.color import RGBColor
except ImportError:
    print("Instalando dependências...")
    os.system("pip install PyPDF2 python-pptx")
    from PyPDF2 import PdfReader
    from pptx import Presentation
    from pptx.util import Inches, Pt
    from pptx.enum.text import PP_ALIGN
    from pptx.dml.color import RGBColor


class PDFToSlidesConverter:
    def __init__(self, pdf_path: str):
        self.pdf_path = pdf_path
        self.presentation = Presentation()
        self.presentation.slide_width = Inches(10)
        self.presentation.slide_height = Inches(7.5)

    def extract_text_from_pdf(self) -> List[dict]:
        """Extrai texto estruturado do PDF"""
        pages_content = []

        pdf_reader = PdfReader(self.pdf_path)
        for page_num, page in enumerate(pdf_reader.pages, 1):
            text = page.extract_text()

            pages_content.append({
                'page_num': page_num,
                'text': text,
                'tables': None
            })

        return pages_content

    def create_title_slide(self, title: str, subtitle: str = ""):
        """Cria slide de título"""
        slide = self.presentation.slides.add_slide(
            self.presentation.slide_layouts[6]  # Blank layout
        )

        # Adiciona background
        background = slide.background
        fill = background.fill
        fill.solid()
        fill.fore_color.rgb = RGBColor(31, 78, 121)  # Azul professional

        # Título
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(2.5), Inches(9), Inches(1.5))
        title_frame = title_box.text_frame
        title_frame.text = title
        title_frame.word_wrap = True

        title_paragraph = title_frame.paragraphs[0]
        title_paragraph.font.size = Pt(54)
        title_paragraph.font.bold = True
        title_paragraph.font.color.rgb = RGBColor(255, 255, 255)
        title_paragraph.alignment = PP_ALIGN.CENTER

        # Subtitle
        if subtitle:
            subtitle_box = slide.shapes.add_textbox(Inches(0.5), Inches(4.2), Inches(9), Inches(1))
            subtitle_frame = subtitle_box.text_frame
            subtitle_frame.text = subtitle
            subtitle_paragraph = subtitle_frame.paragraphs[0]
            subtitle_paragraph.font.size = Pt(24)
            subtitle_paragraph.font.color.rgb = RGBColor(200, 200, 200)
            subtitle_paragraph.alignment = PP_ALIGN.CENTER

    def create_content_slide(self, title: str, content: str):
        """Cria slide com conteúdo"""
        slide = self.presentation.slides.add_slide(
            self.presentation.slide_layouts[6]  # Blank layout
        )

        # Título
        title_box = slide.shapes.add_textbox(Inches(0.5), Inches(0.5), Inches(9), Inches(0.8))
        title_frame = title_box.text_frame
        title_frame.text = title
        title_paragraph = title_frame.paragraphs[0]
        title_paragraph.font.size = Pt(40)
        title_paragraph.font.bold = True
        title_paragraph.font.color.rgb = RGBColor(31, 78, 121)

        # Conteúdo
        content_box = slide.shapes.add_textbox(Inches(0.5), Inches(1.5), Inches(9), Inches(5.5))
        text_frame = content_box.text_frame
        text_frame.word_wrap = True

        # Divide o conteúdo em parágrafos
        paragraphs = content.split('\n')
        for i, paragraph_text in enumerate(paragraphs):
            if i > 0:
                text_frame.add_paragraph()

            paragraph = text_frame.paragraphs[i]
            paragraph.text = paragraph_text.strip()
            paragraph.level = 0
            paragraph.font.size = Pt(14)
            paragraph.font.color.rgb = RGBColor(0, 0, 0)
            paragraph.space_before = Pt(6)
            paragraph.space_after = Pt(6)

    def convert(self, output_path: str = None):
        """Converte PDF para apresentação PPTX"""
        if output_path is None:
            output_path = self.pdf_path.replace('.pdf', '_converted.pptx')

        print(f"📄 Extraindo conteúdo de {self.pdf_path}...")
        pages_content = self.extract_text_from_pdf()

        print(f"📊 Criando apresentação com {len(pages_content)} slides...")

        # Slide de título
        pdf_name = Path(self.pdf_path).stem
        self.create_title_slide(pdf_name, "Convertido automaticamente de PDF")

        # Slides de conteúdo
        for page_data in pages_content:
            text = page_data['text']
            if text and text.strip():
                # Toma as primeiras linhas como título
                lines = text.split('\n')
                title = lines[0][:60] if lines else "Página"
                content = '\n'.join(lines[1:]) if len(lines) > 1 else text

                self.create_content_slide(title, content)

        # Salva a apresentação
        self.presentation.save(output_path)
        print(f"✅ Apresentação criada: {output_path}")
        return output_path


def main():
    if len(sys.argv) < 2:
        print("Uso: python pdf_to_slides.py <arquivo.pdf> [output.pptx]")
        print("\nExemplo:")
        print("  python pdf_to_slides.py documento.pdf")
        sys.exit(1)

    pdf_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) > 2 else None

    if not os.path.exists(pdf_path):
        print(f"❌ Erro: Arquivo {pdf_path} não encontrado")
        sys.exit(1)

    converter = PDFToSlidesConverter(pdf_path)
    converter.convert(output_path)


if __name__ == "__main__":
    main()
