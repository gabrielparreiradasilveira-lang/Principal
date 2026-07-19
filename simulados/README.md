# Simulados TopInvest — Sistema de Simulados para Alunos

Aplicação web (HTML/JS puro, sem build step) com Firebase (Auth + Firestore) para:

- **Alunos**: criar conta, ver só as certificações que compraram, fazer a prova com timer (incluindo estudos de caso e árvores de decisão), ver resultado comentado com vídeo-explicação e consultar histórico.
- **Você (admin)**: cadastrar certificações, cadastrar questões (simples, estudo de caso "mãe/filha" ou árvore de decisão), montar simulados, publicar/despublicar, liberar/revogar acesso de cada aluno e acompanhar desempenho.
- **Hotmart**: quando alguém compra na Hotmart, o acesso à certificação correspondente é liberado automaticamente no site (e revogado em caso de reembolso/chargeback), via um webhook separado (pasta `hotmart-webhook/`).

## Arquitetura em 1 minuto

```
simulados/            → o site em si (Firebase Hosting, Auth, Firestore — tudo no plano gratuito)
hotmart-webhook/       → 1 função serverless na Vercel (grátis) que recebe o aviso da Hotmart
                         e usa o Firebase Admin SDK para liberar/revogar acesso no Firestore
```
O Firebase fica 100% no plano gratuito (Spark, sem cartão) porque quem precisa de um servidor
"de verdade" — o webhook da Hotmart — roda fora dele, na Vercel.

## 1. Criar o projeto no Firebase

1. Acesse https://console.firebase.google.com e crie um novo projeto (plano Spark, gratuito).
2. No menu lateral, ative:
   - **Authentication** → método "E-mail/senha".
   - **Firestore Database** → criar banco em modo produção (as regras já vêm neste projeto).
3. Em "Configurações do projeto" → "Seus apps" → ícone `</>` (Web) para criar um app web e copiar as credenciais (`apiKey`, `authDomain`, etc).
4. Cole essas credenciais em `simulados/js/firebase-config.js`, substituindo os valores `COLOQUE_AQUI`.

## 2. Publicar as regras de segurança do Firestore

No console do Firebase → **Firestore Database → Regras** → cole o conteúdo de `firestore.rules` → Publicar.

Ou via CLI:
```bash
npm install -g firebase-tools
firebase login
firebase init firestore
firebase deploy --only firestore:rules
```

## 3. Hospedar o site

```bash
firebase init hosting   # public directory = "simulados"
firebase deploy --only hosting
```
Também funciona em Netlify/Vercel/GitHub Pages apontando para a pasta `simulados/`.

Para testar localmente:
```bash
cd simulados
python3 -m http.server 8080
# abra http://localhost:8080
```
(Precisa de servidor HTTP, não abrir o `index.html` direto no navegador — por causa dos módulos ES.)

## 4. Criar seu usuário administrador

1. Cadastre-se normalmente no site publicado (isso te cria como "aluno").
2. Firestore → coleção `users` → seu documento (mesmo e-mail) → edite `role` de `"aluno"` para `"admin"`.
3. Recarregue o site logado — o menu vira "Admin".

## 5. Como usar o painel admin

1. **Certificações** → cadastre "CPA-20", "CPA-10", "CEA" etc., com o link de compra na Hotmart (opcional, aparece pro aluno sem acesso).
2. **Questões** → escolha a certificação, "+ Nova questão" e o tipo:
   - **Simples**: enunciado + alternativas + gabarito, como um múltipla-escolha comum.
   - **Estudo de caso (mãe/filha)**: um contexto (ex: perfil de um cliente fictício) com várias perguntas ligadas a ele.
   - **Árvore de decisão**: uma situação inicial com várias interações em sequência; você define quantos acertos são necessários para o aluno "passar" naquele item.
   - Em qualquer tipo dá pra anexar um vídeo-explicação (URL) e o nome do professor.
3. **Simulados** → escolha a certificação, monte o simulado marcando as questões, defina tempo/nota de corte e publique.
4. **Alunos** → veja desempenho e, na mesma tela, marque/desmarque manualmente o acesso de cada aluno a cada certificação (útil antes de configurar a Hotmart, ou pra liberar um caso avulso).

## 6. Ligar a Hotmart (liberação automática de acesso)

Sem isso, você ainda pode liberar acesso manualmente em **Alunos** — a Hotmart só automatiza.

1. **Gerar a chave de serviço do Firebase**: Console do Firebase → Configurações do projeto → Contas de serviço → "Gerar nova chave privada" (baixa um `.json`).
2. **Publicar o webhook na Vercel** (grátis, sem cartão):
   ```bash
   cd hotmart-webhook
   npm install -g vercel   # se ainda não tiver
   vercel deploy --prod
   ```
3. Na Vercel, configure as variáveis de ambiente do projeto (Settings → Environment Variables) — veja `hotmart-webhook/.env.example`:
   - `FIREBASE_SERVICE_ACCOUNT_BASE64`: rode `base64 -i chave.json | tr -d '\n'` e cole o resultado.
   - `HOTMART_HOTTOK`: veja o passo 4 abaixo.
   - `HOTMART_PRODUCT_MAP`: ex. `{"123456":"CPA-20"}` — mapeia o ID do produto na Hotmart para o **nome exato** da certificação cadastrada no passo 5.1.
4. **Configurar o webhook na Hotmart**: painel da Hotmart → Ferramentas → Webhook → Adicionar → cole a URL que a Vercel te deu (`https://seu-projeto.vercel.app/api/hotmart`) → copie o "Hottok" gerado e cole em `HOTMART_HOTTOK` → marque os eventos: Compra aprovada, Compra completa, Compra cancelada, Reembolso, Chargeback.
5. Redeploy o webhook depois de configurar as variáveis (`vercel deploy --prod`).

Fluxo resultante: aluno compra na Hotmart → webhook libera o acesso (se ele já tem conta no site,
libera na hora; se ainda não criou conta, fica "reservado" e é aplicado automaticamente no
cadastro) → aluno vê a certificação desbloqueada no site.

## Estrutura de dados (Firestore)

- `users/{uid}`: `{ name, email, role: 'aluno'|'admin', purchasedCertifications: [certificationId,...], lastDeviceId, deviceSwitchCount }`
- `certifications/{id}`: `{ name, checkoutUrl }`
- `pendingAccess/{emailLowercased}`: `{ certifications: [certificationId,...] }` — acesso "reservado" pela Hotmart antes do cadastro; aplicado e apagado no signup.
- `questions/{id}`: ver comentário no topo de `js/db.js` — varia por `type: "simples" | "mae" | "filha" | "arvore"`.
- `exams/{id}`: `{ certificationId, title, description, timeLimitMinutes, passScorePercent, questionIds[], shuffleQuestions, published }`
- `attempts/{id}`: `{ userId, userName, examId, examTitle, certificationId, answers, correctCount, totalCount, scorePercent, passed, finishedAt }`

## Limitações conhecidas (e como evoluir depois)

- **Correção no cliente**: o navegador do aluno recebe o gabarito para calcular a nota (sem servidor próprio no app principal). Um aluno tecnicamente curioso poderia inspecionar a rede e ver respostas antes de terminar. Para provas de alto risco, dá pra mover a correção para uma Cloud Function — mas aí entra o plano pago do Firebase, que você pediu pra evitar por ora.
- **Trava de dispositivo é só um aviso**: como não estamos usando Cloud Functions, não é possível bloquear de fato um segundo dispositivo — o sistema detecta e avisa (e mostra pro admin quantas trocas aconteceram), mas um usuário determinado pode contornar. Se isso virar um problema real, a solução correta é mover essa checagem para o backend (Cloud Functions ou o próprio webhook), o que exige o plano Blaze.
- **Gate de acesso por certificação também é de UI**, não de regra de banco linha-a-linha: as regras do Firestore impedem o aluno de editar `purchasedCertifications` dele mesmo, mas não impedem tecnicamente que ele leia o conteúdo de um exame publicado se souber o ID (a tela normal não mostra isso). Suficiente pra maioria dos casos; não é DRM real.
- **Sem reentrada em simulado**: se o aluno fechar a aba no meio da prova, o progresso daquela tentativa se perde. Dá pra evoluir salvando respostas parciais no Firestore a cada resposta.
- **Árvore de decisão é sequencial, não ramificada de verdade**: cada interação é fixa (não muda o próximo passo dependendo da resposta) — conta acertos ao longo de um caminho único, o que cobre o caso de uso mas é mais simples que o sistema original.
- **Sem moderação de questões** (reportadas pelo aluno, "difíceis", estatística de erro por questão): você pediu pra deixar de fora por agora.
- **Importação em massa de questões**: cadastro é manual, formulário por questão.

## Dúvidas / próximos passos sugeridos

- Quer um domínio próprio (ex: simulados.suaescola.com.br)? Dá pra configurar no Firebase Hosting.
- Quer que eu adicione importação de questões via planilha?
- Quer moderação (questões reportadas, estatística de acerto por questão) depois de tudo validado?
