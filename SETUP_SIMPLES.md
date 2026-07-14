# 🚀 Setup Simples - Sem Google Cloud Console!

Apenas **3 passos** e você fica pronto!

---

## Passo 1️⃣: Criar Credenciais OAuth (5 min)

1. Vá para: https://myaccount.google.com/
2. Clique em **"Segurança"** (menu esquerdo)
3. Procure por **"Aplicativos e sites com acesso"**
4. Clique em **"Gerencie todas as versões"**
5. **OU** vá direto para: https://console.cloud.google.com/apis/credentials

### Na página de Credenciais:

1. Clique em **"+ Criar Credenciais"**
2. Escolha: **"OAuth 2.0 - ID do cliente"**
3. Tipo de aplicativo: **"Aplicativo para desktop"**
4. Clique em **"Criar"**
5. Clique no botão para **"Download JSON"** (ícone de seta para baixo)

**Arquivo baixado:** `client_secret_[...].json`

---

## Passo 2️⃣: Renomear e Colocar na Pasta

Renomeie o arquivo para: **`credentials_oauth.json`**

Coloque na mesma pasta que o script:

```
Principal/
├── converter_simples.py
├── credentials_oauth.json  ← Aqui!
└── seu_documento.pdf
```

---

## Passo 3️⃣: Compartilhar Seu Template

1. Abra seu template no Google Slides:
   https://docs.google.com/presentation/d/1_M9kVI00iLgRO1IHITh5LWAuH48febps-tSUjEZ9V90/

2. Clique em **"Compartilhar"** (canto superior direito)

3. Digite seu **próprio email** (o mesmo que usa no Google)

4. Permissão: **"Editor"**

5. Clique em **"Compartilhar"**

✅ **Pronto! Seu template pode ser clonado**

---

## 🎯 Usar o Script

### Primeira Vez (com autorização):

```bash
python converter_simples.py aula1.pdf
```

**O que acontece:**
1. ✅ Abre o navegador
2. ✅ Você clica em "Autorizar"
3. ✅ Salva o token automaticamente
4. ✅ Cria o slide no Google Drive

### Próximas Vezes (automático):

```bash
python converter_simples.py aula2.pdf
python converter_simples.py aula3.pdf
```

**Sem precisar autorizar de novo!** 🚀

---

## 📋 Resultado

```
python converter_simples.py documento.pdf

[Output]
============================================================
  PDF → Google Slides
============================================================

📄 Extraindo: documento.pdf...
✅ 13 páginas extraídas

📋 Clonando template...
✅ Template clonado!

✍️  Preenchendo 13 slides...
✅ Slides preenchidos!

============================================================
🎉 PRONTO! Seu slide foi criado no Google Drive!
============================================================

🔗 Abra aqui:
   https://docs.google.com/presentation/d/[ID]/edit
```

---

## ⚡ Dicas

### Mudar o Template
Se quiser usar outro template:

1. Abra seu novo template no Google Slides
2. Copie o ID da URL:
   ```
   https://docs.google.com/presentation/d/[ESTE_ID_AQUI]/edit
   ```
3. Edite `converter_simples.py` linha ~20:
   ```python
   TEMPLATE_ID = "[NOVO_ID_AQUI]"
   ```

### Permissões
Se aparecer erro de permissão:
1. Certifique-se que compartilhou o template com você mesmo
2. Ou tente autorizar novamente (delete `token.pickle`)

### Deletar Token
Para refazer a autenticação:
```bash
rm token.pickle
python converter_simples.py documento.pdf
```

---

## 🆘 Troubleshooting

### "credentials_oauth.json not found"
- Certifique-se que renomeou o arquivo para `credentials_oauth.json`
- Está na mesma pasta que `converter_simples.py`?

### "403 Forbidden"
- Você compartilhou seu template com você mesmo?
- Tente compartilhar novamente

### "No module named 'google'"
```bash
pip install google-auth-oauthlib google-auth-httplib2 google-api-python-client PyPDF2
```

---

## ✅ Checklist

- [ ] Baixei `client_secret_[...].json`
- [ ] Renomeei para `credentials_oauth.json`
- [ ] Coloquei na pasta `Principal/`
- [ ] Compartilhei meu template com meu próprio email
- [ ] Testei com: `python converter_simples.py meu_pdf.pdf`
- [ ] Sucesso! 🎉

---

**Pronto! Agora é só enviar PDF e converter! 🚀**
