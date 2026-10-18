# Plano 001

1. **Fonte.** Exportação em texto do original (`doc18.txt`, scratchpad). As tabelas e a estrutura são copiadas dela.
2. **Conteúdo.** Um MD por aula em `aulas-certificacoes/roteiros/cpa/guias-15-10/`, no dialeto:
   - `#`, `##`, `###`, `####` = títulos 1 a 4;
   - `- **Marcador**` = marcador nível 1; `  - "fala"` = fala nível 2;
   - `>` = frase de fixação;
   - `1.` = lista numerada;
   - `|` = tabela;
   - `🔗 Ponte:` = parágrafo de ponte.
3. **Gerador** (`build_tab.py`):
   - MD → `update_doc` requests para uma guia (tabId);
   - inserções em ordem crescente com cursor UTF-16; tabelas pela fórmula `i + 4 + r(2C + 1) + 2c`;
   - estilos depois; bullets por último, em ordem decrescente de índice (os tabs de aninhamento encolhem o texto).
4. **Montagem.** Renomear a guia padrão e criar as outras 5. Uma chamada por guia.
5. **Verificação.** Exportar o texto e conferir, por guia, os títulos, a contagem de tabelas e a ausência de mojibake.
