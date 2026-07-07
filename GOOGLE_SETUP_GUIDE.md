# 🔐 Setup Google Cloud - Guia Completo

Para usar o conversor com seu template do Google Slides, você precisa configurar credenciais do Google.

## ⚡ Setup Rápido (5 minutos)

### 1️⃣ Criar Projeto no Google Cloud

1. Vá para: https://console.cloud.google.com/
2. Clique em "Selecionar um projeto" (canto superior esquerdo)
3. Clique em "NOVO PROJETO"
4. Nome: `PDF to Slides` (ou seu preferido)
5. Clique em "CRIAR"

### 2️⃣ Habilitar APIs

1. No menu superior, procure por: **APIs e serviços**
2. Clique em **"Ativar APIs e serviços"**
3. Procure por: `Google Slides API`
   - Clique e ative
4. Procure por: `Google Drive API`
   - Clique e ative

### 3️⃣ Criar Service Account

1. Vá para: **APIs e serviços** → **Credenciais**
2. Clique em **"Criar Credenciais"** → **"Conta de Serviço"**
3. Preencha:
   - Nome da conta: `pdf-to-slides`
   - Clique em **"Criar e Continuar"**
4. Pule as próximas etapas (opcional)
5. Clique em **"Concluído"**

### 4️⃣ Gerar Chave JSON

1. Na página de Credenciais, clique em **"Contas de serviço"**
2. Clique no email da conta criada
3. Vá para aba **"Chaves"**
4. Clique em **"Adicionar chave"** → **"Criar nova chave"**
5. Selecione **JSON**
6. Clique em **"Criar"**

**Arquivo `credentials.json` foi baixado automaticamente!** 📥

### 5️⃣ Compartilhar seu Template

1. Abra seu template no Google Slides:
   https://docs.google.com/presentation/d/1_M9kVI00iLgRO1IHITh5LWAuH48febps-tSUjEZ9V90/edit

2. Clique em **"Compartilhar"** (canto superior direito)

3. Copie o email da Service Account (está no arquivo JSON baixado, campo "client_email")

4. Cole o email na caixa de compartilhamento

5. Dê permissão de **"Editor"**

6. Clique em **"Compartilhar"**

---

## 🚀 Usando o Script

### Coloque o arquivo `credentials.json` na pasta do projeto:

```bash
# Estrutura esperada:
Principal/
├── pdf_to_google_slides_template.py
├── credentials.json  ← Arquivo baixado
└── seu_documento.pdf
```

### Execute o conversor:

```bash
python pdf_to_google_slides_template.py seu_documento.pdf credentials.json
```

### Resultado:

```
✅ Template clonado
✅ Conteúdo preenchido
✅ Arquivo salvo no Google Drive

🔗 https://docs.google.com/presentation/d/[ID]/edit
```

---

## 📂 Salvar em Pasta Específica (Opcional)

Se quiser salvar em uma pasta específica do Drive:

```bash
python pdf_to_google_slides_template.py seu_documento.pdf credentials.json [FOLDER_ID]
```

### Como obter o FOLDER_ID:

1. Abra a pasta no Google Drive
2. Veja a URL:
   ```
   https://drive.google.com/drive/folders/[FOLDER_ID]
   ```
3. Copie o `[FOLDER_ID]`

---

## ✅ Checklist

- [ ] Projeto criado no Google Cloud Console
- [ ] Google Slides API ativada
- [ ] Google Drive API ativada
- [ ] Service Account criada
- [ ] credentials.json baixado
- [ ] credentials.json colocado na pasta do projeto
- [ ] Email da Service Account compartilhado no template
- [ ] Script testado com seu PDF

---

## 🆘 Troubleshooting

### Erro: "401 Unauthorized"
- Verifique se compartilhou seu template com o email da Service Account
- Email está em: `credentials.json` → procure por `"client_email"`

### Erro: "403 Forbidden"
- Certifique-se que as APIs estão ativadas
- Vá para: https://console.cloud.google.com/apis/dashboard

### Arquivo credentials.json não encontrado
- Certifique-se que está na mesma pasta que o script
- Ou passe o caminho completo:
  ```bash
  python pdf_to_google_slides_template.py documento.pdf /caminho/para/credentials.json
  ```

### Apresentação não aparece no Drive
- Verifique se a pasta foi especificada corretamente
- Tente sem especificar pasta (vai salvar em "Meus arquivos")

---

## 🔒 Segurança

⚠️ **IMPORTANTE:**
- Nunca compartilhe seu arquivo `credentials.json`
- Não faça commit desse arquivo no GitHub
- Adicione a .gitignore:

```bash
echo "credentials.json" >> .gitignore
git add .gitignore
git commit -m "Add credentials.json to gitignore"
```

---

## 📚 Recursos

- Google Cloud Console: https://console.cloud.google.com/
- Google Slides API Docs: https://developers.google.com/slides
- Google Drive API Docs: https://developers.google.com/drive

---

**Pronto! Agora seu PDF será convertido direto no Google Slides com seu template!** 🎉
