# ⚡ Autorização Rápida (2 minutos)

## Passo 1: Crie as Credenciais OAuth (1 min)

### Vá para este link:
https://console.cloud.google.com/apis/credentials

### Se pedir para criar projeto:
1. Clique em **"Criar Projeto"**
2. Nome: `PDF to Slides`
3. Clique **"Criar"**

### Na página de Credenciais:

1. Clique em **"+ Criar Credenciais"**
2. Escolha: **"OAuth 2.0 - ID do cliente"**
3. **Tipo de aplicativo:** "Aplicativo para desktop"
4. Clique em **"Criar"**
5. Clique no botão de **Download** (ícone de seta para baixo)

### Arquivo baixado:
- Nome será algo como: `client_secret_XXXXX.json`
- **Renomeie para:** `credentials_oauth.json`

---

## Passo 2: Ative as APIs (30 segundos)

Na mesma página, procure por **"Ativar APIs"**

Ative estas duas:
1. **Google Slides API**
2. **Google Drive API**

---

## Passo 3: Compartilhe seu Template (30 segundos)

1. Abra seu template:
   https://docs.google.com/presentation/d/1_M9kVI00iLgRO1IHITh5LWAuH48febps-tSUjEZ9V90/

2. Clique em **"Compartilhar"** (canto superior direito)

3. Digite seu **próprio email** (o mesmo Google que você usa)

4. Permissão: **"Editor"**

5. Clique em **"Compartilhar"**

---

## Passo 4: Envie o Arquivo para Cá

1. Coloque `credentials_oauth.json` na pasta `Principal/`
2. **OU** envie o arquivo aqui na conversa
3. Me avise quando estiver pronto!

---

**Pronto! Isso é tudo! Depois eu crio os slides automaticamente!** ✅
