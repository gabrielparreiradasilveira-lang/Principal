const fs = require("fs");
const path = require("path");
const { THEME, makeDeck, R } = require("./lib.js");
const S = require("./slides.js");
const { applyTheme } = require(process.env.SKILL + "/scripts/apply_theme.js");

const OUT = process.argv[2];
const LOGO = path.join(OUT, "logo-x8.png");
const DECK = path.join(OUT, "C-PRO_R_Aula_3_Capacidade_poupanca_liquidez.pptx");
const MD = path.join(OUT, "roteiro-aula-3.md");

const fmt = (t) => String(t).replace(".", ",");
const LABELS = [["explicacao", "EXPLICAÇÃO"], ["exemplo", "EXEMPLO"], ["conducao", "CONDUÇÃO"], ["prova", "NA PROVA"], ["gabarito", "GABARITO"]];

function notesText(s) {
  const parts = [`TEMPO: ${fmt(s.time)} min`, `RECURSO VISUAL: ${s.visual}`];
  for (const [k, l] of LABELS) if (s.notes[k]) parts.push(`${l}: ${s.notes[k]}`);
  return parts.join("\n\n");
}

// texto visível ao aluno, para o roteiro em Markdown
function visible(s) {
  const L = [];
  const q = (t) => t.replace(/\n+/g, " / ");
  switch (s.type) {
    case "capa": L.push(s.kicker, q(s.title)); if (s.sub) L.push(s.sub); if (s.sign.trim()) L.push(s.sign); break;
    case "flow": if (s.case) L.push(s.case); s.cards.forEach((c, i) => L.push(`${c.n || String(i + 1).padStart(2, "0")} · **${c.t}**: ${q(c.d)}`)); if (s.foot) L.push(s.foot); break;
    case "compare": if (s.lead) L.push(s.lead); [s.left, s.right].forEach((c) => L.push(`**${c.t}**: ${c.items.join(" · ")}`)); break;
    case "concept": L.push(`**${s.l1 || "O QUE É"}**: ${q(s.what)}`, `**${s.l2 || "NA FALA DO CLIENTE"}**: ${q(s.say)}`, `**${s.l3 || "COMO AGIR"}**: ${q(s.act)}`); break;
    case "dialog": s.lines.forEach((l) => L.push(`**${l.who}**: ${l.t}`)); (s.defs || []).forEach((d) => L.push(`**${d.k}**: ${d.v}`)); break;
    case "stats": if (s.case) L.push(s.case); s.cards.forEach((c) => L.push(`**${c.k}**${c.line ? " (" + c.line + ")" : ""}: ${c.big}, ${c.sub}`)); break;
    case "grid": s.cards.forEach((c) => L.push(`${c.n} · **${c.t}**: ${c.d}`)); break;
    case "table": L.push("| " + s.cols.join(" | ") + " |", "| " + s.cols.map(() => "---").join(" | ") + " |", ...s.rows.map((r) => "| " + r.join(" | ") + " |")); break;
    case "question": L.push(s.case, `**${s.ask}**`, ...s.alts.map((a, i) => `${"ABCD"[i]}) ${a}`)); break;
    case "review": s.items.forEach((t, i) => L.push(`${String(i + 1).padStart(2, "0")}. ${t}`)); break;
    case "quiz": s.items.forEach((t, i) => L.push(`${i + 1}. ${t}`)); L.push(s.foot); break;
  }
  if (s.band) L.push(`**Na prova**: ${s.band}`);
  return s.type === "table" ? L.join("\n") : L.map((l) => (l.startsWith("|") ? l : "- " + l)).join("\n");
}

(async () => {
  const { pres, C } = makeDeck({ title: "C-PRO R · Aula 3", logo: LOGO, footer: "X8 EDUCAÇÃO  ·  C-PRO R  ·  AULA 3" });
  let current = null;
  S.forEach((s) => {
    if (s.section !== current) { pres.addSection({ title: s.section }); current = s.section; }
    const slide = R[s.type](pres, C, s);
    slide.addNotes(notesText(s));
  });
  await pres.writeFile({ fileName: DECK });
  await applyTheme(DECK, THEME);

  // ---------- roteiro em Markdown ----------
  const total = S.reduce((a, s) => a + s.time, 0);
  const blocks = [];
  S.forEach((s, i) => {
    let b = blocks.find((x) => x.name === s.section);
    if (!b) { b = { name: s.section, slides: [], time: 0 }; blocks.push(b); }
    b.slides.push(i + 1); b.time += s.time;
  });
  const qIdx = S.map((s, i) => (s.type === "question" ? i + 1 : 0)).filter(Boolean);
  const pIdx = S.map((s, i) => (/PERGUNTA RÁPIDA/.test(s.tag || "") ? i + 1 : 0)).filter(Boolean);
  const out = [];
  out.push("# C-PRO R · Aula 3: quanto sobra, quanto dura e quão rápido vira dinheiro", "");
  out.push(`Itens **2.1 e 2.2** do programa detalhado ANBIMA (v1.2, vigência a partir de 01/01/2026) · **${fmt(total)} min ao vivo** · **${S.length} slides** · identidade visual X8`, "");
  out.push("## 1. Roteiro da aula (distribuição dos 60 minutos)", "");
  out.push("| Bloco | Slides | Tempo | Conteúdo |", "| --- | --- | --- | --- |");
  const desc = {
    "Abertura": "Capa, mapa da aula e caso da Marina (pergunta rápida)",
    "Bloco 1 · 2.1.1 a 2.1.4": "Capacidade de poupança, renda, idade e padrão de vida, estratégias, planejamento, poupança do país (IBGE) e reserva de emergência + questão 1",
    "Bloco 2 · 2.1.5 a 2.1.7": "Balanço da Marina, ativos de uso e não uso, PL, cobertura de despesas e índice de poupança + certo ou errado + questão 2",
    "Bloco 3 · 2.2.1 a 2.2.4": "Conceito de liquidez, liquidez e reserva, liquidez × rentabilidade, liquidez corrente e seca + questão 3",
    "Revisão": "Cinco ideias, questão integradora (resposta ao caso) e encerramento",
  };
  blocks.forEach((b) => out.push(`| ${b.name} | ${b.slides[0]}–${b.slides[b.slides.length - 1]} | ${fmt(b.time)} min | ${desc[b.name]} |`));
  out.push(`| **Total** | **${S.length}** | **${fmt(total)} min** | |`, "");
  out.push(`**Interação prevista:** perguntas rápidas (slides ${pIdx.join(" e ")}) e ${qIdx.length} questões autorais (slides ${qIdx.join(", ")}), com gabarito comentado nas notas. Caso único: Marina, 36 anos, CLT, um filho.`, "");
  out.push("## 2. Slides", "");
  S.forEach((s, i) => {
    out.push(`### Slide ${i + 1} · ${s.title.replace(/\n/g, " ")}`, "");
    out.push(`**Bloco:** ${s.section} · **Tempo:** ${fmt(s.time)} min${s.tag ? " · **Etiqueta:** " + s.tag : ""}`, "");
    out.push("**Conteúdo visível:**", "", visible(s), "");
    out.push(`**Recurso visual:** ${s.visual}`, "");
    out.push("**Notas do professor:**", "");
    for (const [k, l] of LABELS) if (s.notes[k]) out.push(`- **${l[0] + l.slice(1).toLowerCase()}:** ${s.notes[k].replace(/\n/g, " / ")}`);
    out.push("", "---", "");
  });

  out.push("## 3. Fontes conferidas e correções nos materiais", "");
  out.push(
    "**Fontes conferidas (27/10/2026):**", "",
    "- Programa Detalhado C-PRO R (ANBIMA, v1.2, rev. 04/06/2025, vigência a partir de 01/01/2026), itens 2.1 a 2.1.7 e 2.2 a 2.2.4 (Módulo 2 = 20% do programa).",
    "- Apostila C-PRO R (Top Invest, rev. mar/2026), p. 85 a 89, inclusive as fórmulas em imagem do índice de poupança (p. 88) e da liquidez corrente (p. 89).",
    "- Slides X8 do Módulo 2: A5125 (capacidade de poupança), A5126 (balanço patrimonial pessoal) e A5127 (indicadores de liquidez).",
    "- IBGE, Contas Nacionais Trimestrais, SIDRA tabela 6726 (taxa de poupança) e 6727 (taxa de investimento), com PIB trimestral da tabela 2072. Taxa de poupança de 2025 recomposta pela média dos trimestres ponderada pelo PIB: **14,4%** (2024: 14,1%), igual à divulgada pelo IBGE em 03/03/2026. Taxa de investimento de 2025: **16,8%**, segundo o release do IBGE (a média ponderada do SIDRA dá 16,9%, diferença de arredondamento).", "",
    "**Correções e convenções em relação aos materiais de origem:**", "",
    "| Fonte | O material diz | O correto ou a convenção adotada |",
    "| --- | --- | --- |",
    "| Slide X8 A5125-7 | Reserva por perfil de suitability: conservador 12 meses, moderado 6, arrojado 3 a 4 | A apostila liga o tamanho da reserva a **estabilidade da renda, profissão, dependentes e despesas fixas**, e não ao perfil de risco. Faixas usadas como **prática de mercado**: 3 a 6 meses (renda estável) e até 12 (renda variável) |",
    "| Apostila p. 89 | Liquidez seca sem fórmula | Convenção do material X8 (A5127-8): **ativos de resgate imediato ÷ passivos de curto prazo**. Sem força normativa |",
    "| Slide X8 A5127-6 × A5127-9 | A corrente usa \"dinheiro e aplicações acessados rapidamente\" e, no quadro, \"todos os ativos de curto prazo\" | Regra coerente adotada: **corrente = todos os ativos de curto prazo (até 12 meses); seca = só os de resgate imediato** |",
    "| Apostila p. 87 | Cobertura de despesas sem fórmula (\"patrimônio disponível\") | Convenção X8 (A5126-5): **ativos líquidos ÷ despesa mensal** |",
    "| Slide X8 A5127-5 | Taxas de exemplo (Tesouro Selic 10,65%, CDB 3 anos 12,20%) | Não usadas: envelhecem com o cenário. A tabela de liquidez × rentabilidade é qualitativa |",
    "| Apostila p. 88–89 | Subitens 2.2.1 a 2.2.4 numerados todos como \"2.2\" | Numeração do PD |", "",
    "**Pendências:**", "",
    "- Limite de cobertura do FGC: citado só como \"até um limite por CPF e instituição\"; conferir o valor vigente na Res. CMN 4.222/2013 antes de dizer o número em aula.",
    "- Sequências da HP12C das notas: não testadas em aparelho.", "");
  fs.writeFileSync(MD, out.join("\n"));
  console.log("ok", DECK, MD, "total", total, "slides", S.length);
})();
