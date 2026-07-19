# Simulados TopInvest — Sistema de Simulados para Alunos

Aplicação web simples (HTML/JS puro, sem build step) com Firebase (Auth + Firestore) para:

- **Alunos**: criar conta, escolher um simulado por certificação (CPA-10, CPA-20, CEA ou qualquer outra que você cadastrar), fazer a prova com timer, ver resultado comentado e consultar histórico de tentativas.
- **Você (admin)**: cadastrar certificações, cadastrar questões (enunciado, alternativas, gabarito, explicação, módulo/tema), montar simulados selecionando quais questões entram, definir tempo limite e nota de corte, publicar/despublicar, e acompanhar o desempenho de cada aluno.

## 1. Criar o projeto no Firebase

1. Acesse https://console.firebase.google.com e crie um novo projeto (gratuito, plano Spark serve para começar).
2. No menu lateral, ative:
   - **Authentication** → método "E-mail/senha".
   - **Firestore Database** → criar banco em modo produção (as regras já vêm neste projeto).
3. Em "Configurações do projeto" → "Seus apps" → clique no ícone `</>` (Web) para criar um app web e copiar as credenciais (`apiKey`, `authDomain`, etc).
4. Cole essas credenciais em `simulados/js/firebase-config.js`, substituindo os valores `COLOQUE_AQUI`.

## 2. Publicar as regras de segurança do Firestore

No console do Firebase, vá em **Firestore Database → Regras** e cole o conteúdo do arquivo `firestore.rules` deste projeto. Clique em "Publicar".

Se preferir usar a CLI do Firebase:
```bash
npm install -g firebase-tools
firebase login
firebase init firestore   # aponte para este projeto, aceite os arquivos padrão
firebase deploy --only firestore:rules
```

## 3. Hospedar o site

A forma mais simples é o **Firebase Hosting** (gratuito):
```bash
firebase init hosting   # public directory = "simulados"
firebase deploy --only hosting
```
Você também pode hospedar em qualquer serviço de arquivos estáticos (Netlify, Vercel, GitHub Pages) — é só apontar para a pasta `simulados/`.

Para testar localmente antes de publicar:
```bash
cd simulados
python3 -m http.server 8080
# abra http://localhost:8080
```
(Precisa ser servido por um servidor HTTP, não abrir o `index.html` direto no navegador, por causa dos módulos ES.)

## 4. Criar seu usuário administrador

1. Acesse o site publicado e cadastre-se normalmente (isso cria você como "aluno").
2. No console do Firebase → Firestore Database → coleção `users` → encontre o documento com seu `uid` (mesmo e-mail que você cadastrou).
3. Edite o campo `role` de `"aluno"` para `"admin"`.
4. Recarregue o site logado — você verá o menu "Admin" em vez de "Simulados".

> Você pode repetir esse processo para dar acesso de admin a outras pessoas (ex: outro professor).

## 5. Como usar o painel admin

1. **Certificações** → cadastre "CPA-20", "CPA-10", "CEA" ou qualquer outra prova.
2. **Questões** → escolha a certificação no filtro, clique em "+ Nova questão" e preencha enunciado, alternativas (marque a correta), módulo/tema (opcional) e explicação do gabarito (opcional, aparece na correção do aluno).
3. **Simulados** → escolha a certificação, clique em "+ Novo simulado", defina título, tempo limite, nota de corte, marque as questões que farão parte da prova e ative "Publicado" para os alunos verem.
4. **Alunos** → acompanhe a média e o histórico de tentativas de cada aluno.

## Estrutura de dados (Firestore)

- `users/{uid}`: `{ name, email, role: 'aluno' | 'admin' }`
- `certifications/{id}`: `{ name }`
- `questions/{id}`: `{ certificationId, module, statement, options[], correctIndex, explanation }`
- `exams/{id}`: `{ certificationId, title, description, timeLimitMinutes, passScorePercent, questionIds[], shuffleQuestions, published }`
- `attempts/{id}`: `{ userId, userName, examId, examTitle, certificationId, answers, correctCount, totalCount, scorePercent, passed, finishedAt }`

## Limitações conhecidas (e como evoluir depois)

- **Correção no cliente**: para manter a stack simples (sem servidor próprio), o gabarito é lido pelo navegador do aluno para calcular a nota. Um aluno tecnicamente curioso poderia inspecionar as requisições de rede e ver as respostas corretas antes de terminar. Para uma prova de alto risco (ex: valendo nota oficial), o próximo passo seria mover o cálculo da correção para uma Cloud Function, escondendo `correctIndex` do cliente até a submissão.
- **Sem reentrada em simulado**: se o aluno fechar a aba no meio da prova, o progresso daquela tentativa se perde (não é salvo parcialmente). Dá para evoluir salvando respostas parciais no Firestore a cada resposta.
- **Importação em massa de questões**: hoje o cadastro é manual, um formulário por questão. Se depois você tiver um banco grande em Excel/CSV, é possível adicionar uma tela de importação.

## Dúvidas / próximos passos sugeridos

- Quer um domínio próprio (ex: simulados.suaescola.com.br)? Dá pra configurar isso no Firebase Hosting.
- Quer que eu adicione importação de questões via planilha?
- Quer relatórios mais detalhados por módulo/tema (ex: "aluno erra muito em Fundos de Investimento")?
