# 📄 PDF to Slides Converter

Transforme PDFs em apresentações automaticamente! ✨

## O que foi criado?

Três scripts para converter PDF em apresentações:

### 1️⃣ **pdf_to_slides.py** (Rápido & Simples)
Gera arquivo PowerPoint (.pptx) que você pode editar depois

**Vantagens:**
- ✅ Sem necessidade de autenticação
- ✅ Rápido e simples
- ✅ Arquivo PPTX editável
- ✅ Preserva todo o texto do PDF

**Como usar:**
```bash
python pdf_to_slides.py seu_documento.pdf
```

**Saída:**
```
seu_documento_converted.pptx
```

### 2️⃣ **pdf_to_google_slides_template.py** ⭐ (RECOMENDADO)
Clona seu template Google Slides e preenche com conteúdo do PDF

**Vantagens:**
- ✅ Mantém suas cores, fontes e layout
- ✅ Salva direto no Google Drive
- ✅ Pronto para usar, sem edições manuais
- ✅ Tema idêntico ao que você faz manualmente

**Como usar:**
```bash
python pdf_to_google_slides_template.py seu_documento.pdf credentials.json
```

**Resultado:**
```
Novo arquivo no Google Drive com seu template!
🔗 https://docs.google.com/presentation/d/[ID]/edit
```

📋 **Setup:** Veja `GOOGLE_SETUP_GUIDE.md`

### 3️⃣ **pdf_to_google_slides.py** (Avançado)
Cria apresentação diretamente no Google Slides (requer autenticação)

**Para usar:**
1. Configure Google Cloud Console
2. Crie uma Service Account
3. Execute:
```bash
python pdf_to_google_slides.py seu_documento.pdf credentials.json
```

---

## ⚡ Uso Rápido - Opção Recomendada (Google Slides com Template)

### Passo 1: Setup Google (uma única vez)
```bash
# Veja o guia completo em: GOOGLE_SETUP_GUIDE.md
# Resumo:
# 1. Crie projeto no Google Cloud Console
# 2. Ative Google Slides e Google Drive APIs
# 3. Crie Service Account e baixe credentials.json
# 4. Compartilhe seu template com o email da Service Account
```

### Passo 2: Colocar credentials.json na pasta
```
Principal/
├── pdf_to_google_slides_template.py
├── credentials.json  ← Arquivo baixado
└── documento.pdf
```

### Passo 3: Executar converter
```bash
python pdf_to_google_slides_template.py documento.pdf credentials.json
```

### Passo 4: Resultado!
✅ Apresentação criada no Google Drive
✅ Com seu template (cores, fontes, layout)
✅ Conteúdo preenchido automaticamente
✅ Pronta para usar!

---

## ⚡ Uso Rápido - Alternativa (PowerPoint local)

### Passo 1: Instalar dependências (primeira vez)
```bash
pip install PyPDF2 python-pptx
```

### Passo 2: Converter seu PDF
```bash
python pdf_to_slides.py documento.pdf
```

### Passo 3: Abrir no Google Slides ou PowerPoint
- Arquivo gerado: `documento_converted.pptx`
- Importe no Google Drive e edite!

---

## 🎯 Fluxo de Trabalho Recomendado

```
1. PDF Original
        ↓
2. python pdf_to_slides.py
        ↓
3. arquivo.pptx (gerado)
        ↓
4. Upload no Google Slides/Drive
        ↓
5. Editar e formatar conforme necessário
```

---

## 📊 Exemplo: Seu PDF foi convertido!

**Arquivo original:**
```
Seguradoras_e_Resseguradoras__A3450.pdf (13 páginas)
```

**Resultado:**
```
Seguradoras_e_Resseguradoras__A3450_converted.pptx
✓ 13 slides criados
✓ Todo o texto preservado
✓ Pronto para editar!
```

---

## 🔧 Personalizações Possíveis

Você pode editar `pdf_to_slides.py` para:

### Mudar cores do tema
```python
fill.fore_color.rgb = RGBColor(31, 78, 121)  # Azul
# Mude para RGB de sua preferência
```

### Ajustar tamanhos de fonte
```python
title_paragraph.font.size = Pt(54)  # Título
paragraph.font.size = Pt(14)        # Conteúdo
```

### Incluir logo/imagem
```python
img_path = 'logo.png'
slide.shapes.add_picture(img_path, Inches(0.5), Inches(0.5))
```

---

## 📝 Estrutura dos Slides

### Slide 1: Capa
- Título (nome do PDF)
- Subtítulo: "Convertido automaticamente"

### Slides 2+: Conteúdo
- **Título**: Primeira linha de cada página do PDF
- **Corpo**: Texto completo do PDF formatado

---

## 🆘 Troubleshooting

### Erro: "ModuleNotFoundError"
```bash
pip install PyPDF2 python-pptx
```

### PDF com imagens/tabelas não aparecem
O script extrai principalmente texto. Para manter layout complexo:
1. Use o PPTX gerado como base
2. Adicione manualmente imagens importantes
3. Formatar tabelas no Google Slides

### Arquivo PPTX não abre
- Tente abrir no Google Slides (mais compatível)
- Ou baixe novo arquivo gerado

---

## 🚀 Próximos Passos

### Opção 1: Melhorar o script
- [ ] Extrair e incluir imagens do PDF
- [ ] Detectar títulos automaticamente
- [ ] Criar layout customizado por página

### Opção 2: Usar Google Slides direto
- [ ] Setup Google Cloud Console
- [ ] Usar `pdf_to_google_slides.py`
- [ ] Editar em tempo real na nuvem

### Opção 3: Interface Web
- [ ] Criar aplicação web
- [ ] Upload de PDF via interface
- [ ] Download direto de PPTX

---

## 📚 Recursos

- **PyPDF2 Docs**: https://pypdf2.readthedocs.io/
- **python-pptx Docs**: https://python-pptx.readthedocs.io/
- **Google Slides API**: https://developers.google.com/slides

---

**Criado com ❤️ para transformar seus PDFs em slides!**

Dúvidas? Execute `python pdf_to_slides.py --help`
