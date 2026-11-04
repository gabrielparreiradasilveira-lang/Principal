# Analogias: método e banco

## O método (seis passos)

Uma analogia só ensina se o aluno souber exatamente o que corresponde a quê e onde a comparação para de valer. Sem isso, ele leva para a prova características da metáfora que o conceito não tem.

1. **Apresente o conceito-alvo** em uma frase técnica.
2. **Evoque a situação familiar** ("você já pagou pedágio...").
3. **Liste os elementos** da situação familiar que importam (2 a 4 por vídeo; até 7 na série inteira).
4. **Mapeie um a um**: elemento → conceito. Escolha a analogia pela **relação** (o que causa o quê, o que aumenta quando o outro diminui) e não pela aparência. Duas coisas parecidas por fora, mas com mecanismos diferentes, ensinam errado.
5. **Diga onde a analogia quebra**, em uma ou duas frases: "aqui a comparação não serve, porque no mercado...".
6. **Volte ao termo técnico** e a um número: repita a definição sem a metáfora e dê um exemplo numérico curto.

No Bloco 2 (~100 palavras), os passos 2, 4 e 5 são obrigatórios na fala; o 1 e o 6 cabem em uma frase cada, ou passam para o Bloco 3.

Na lousa (pronta, no fundo do slide), a metáfora vem **sempre desenhada**, com o mapa "elemento → conceito" e o que a fala não detalha: uma condição, um número, um segundo exemplo, o erro de quem usa a metáfora ao pé da letra (veja `lousas.md`). Use uma metáfora central por aula e reaproveite-a nos títulos dos subitens do Bloco 3, para o aluno ter um fio só.

Cada entrada abaixo diz o **desenho** que a representa. "Criar" quer dizer que ele ainda não existe: acrescente-o em `scripts/desenhos.py` antes de gerar as lousas (instruções em `lousas.md`, seção 6).

Prefira situações comuns para um adulto brasileiro: pedágio, conta de luz, aluguel, condomínio, supermercado, carro usado, seguro.

## Banco de analogias

Cada entrada traz o mapa e o limite. Adapte os números ao tema e confira as regras em `pontos-volateis.md`.

### Tabela regressiva do IR = escada que desce com o tempo
- **Desenho:** criar `escada` (degraus descendo da esquerda para a direita).
- Degraus → faixas de prazo (até 180, 181–360, 361–720, acima de 720 dias).
- Descer um degrau → alíquota menor (22,5% → 20% → 17,5% → 15%).
- Último degrau → 15%, o piso.
- **Onde quebra:** numa escada, cada degrau é um trecho separado; na tabela, não. A alíquota do degrau em que você está vale para o ganho inteiro: quem resgata com 400 dias paga 17,5% sobre todo o rendimento, e não 22,5% sobre os primeiros 180 dias e 20% sobre os seguintes. Além disso, 15% é o chão, e nem todo produto está nessa escada: ações e isentos para pessoa física (LCI, LCA) seguem outras regras.

### Marcação a mercado = preço do carro usado na tabela FIPE
- **Desenho:** `carro` (existe).
- Carro → título.
- Condição do mercado de usados → taxa de juros do mercado.
- Preço do carro hoje → valor do título marcado a mercado.
- Vender o carro hoje → resgatar o título antes do vencimento.
- **Onde quebra:** o título prefixado levado até o vencimento paga exatamente o valor combinado, não importa o que os juros fizeram no caminho. O carro nunca volta a valer o preço de zero quilômetro.

### Duration = gangorra
- **Desenho:** criar `gangorra` (prancha sobre um apoio central).
- Distância do centro → duration.
- Empurrão → variação da taxa de juros.
- Quanto a ponta sobe ou desce → variação do preço do título.
- Quem senta mais longe do centro balança mais com o mesmo empurrão → título de duration maior oscila mais.
- **Onde quebra:** para variações grandes de juros, o preço não se move na mesma proporção (convexidade). A gangorra serve para movimentos pequenos.

### FGC = seguro com teto por instituição
- **Desenho:** `banco` (existe), com uma moldura ao redor.
- Apólice → garantia do FGC.
- Teto da apólice → limite por CPF e por instituição (confira o valor atual em `pontos-volateis.md`).
- Sinistro → intervenção ou liquidação do banco.
- **Onde quebra:** o investidor não contrata nem paga esse "seguro" diretamente; quem contribui são as instituições. E nem todo produto é coberto: debêntures, CRI, CRA e cotas de fundos ficam de fora. Confira a lista atual de produtos cobertos antes de citar.

### Liquidez = vender um imóvel × sacar da conta
- **Desenho:** `casa` e `dinheiro` (existem), em `comparacao`.
- Sacar da conta corrente → ativo de alta liquidez.
- Vender um imóvel → ativo de baixa liquidez: leva tempo e, para vender rápido, é preciso dar desconto.
- Desconto para vender rápido → deságio.
- **Onde quebra:** liquidez não é uma característica fixa do ativo. Ela depende de haver comprador naquele dia: um título que se vende fácil em mercado calmo pode ficar difícil de vender numa crise.

### Previdência PGBL × VGBL = duas rodovias com pedágio
- **Desenho:** `rodovia_pedagio` (existe), uma em cada coluna do molde `comparacao`.
- Vale-pedágio na entrada → dedução do PGBL (até 12% da renda bruta tributável, na declaração completa).
- Pedágio na saída → IR no resgate.
- Lucro da viagem → rendimentos (base do VGBL) · carga inteira → valor total (base do PGBL).
- **Onde quebra:** a tarifa da saída não é fixa (depende do regime e do prazo), e o vale-pedágio não é de graça: o IR deduzido na entrada é cobrado no resgate. Imposto adiado, não perdoado.
