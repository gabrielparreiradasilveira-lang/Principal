const fs = require("fs");
const path = require("path");
const { THEME, makeDeck, R } = require("./lib.js");
const S = require("./slides.js");
const { applyTheme } = require(process.env.SKILL + "/scripts/apply_theme.js");

const OUT = process.argv[2];
const LOGO = path.join(OUT, "logo-x8.png");
const DECK = path.join(OUT, "C-PRO_R_Aula_2_Investidor_coleta_regras.pptx");
const MD = path.join(OUT, "roteiro-aula-2.md");

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
  const { pres, C } = makeDeck({ title: "C-PRO R · Aula 2", logo: LOGO, footer: "X8 EDUCAÇÃO  ·  C-PRO R  ·  AULA 2" });
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
  const out = [];
  out.push("# C-PRO R · Aula 2: quem é o investidor, como conhecê-lo e que regras seguir", "");
  out.push(`Itens **1.3, 1.5 e 1.6** do programa detalhado ANBIMA (v1.2, vigência a partir de 01/01/2026) · **${fmt(total)} min** · **${S.length} slides** · identidade visual X8`, "");
  out.push("## 1. Roteiro da aula (distribuição dos 90 minutos)", "");
  out.push("| Bloco | Slides | Tempo | Conteúdo |", "| --- | --- | --- | --- |");
  const desc = {
    "Abertura": "Capa, mapa da aula e aquecimento (avó e neto)",
    "Bloco 1 · 1.3.1 a 1.3.4": "Retrato do investidor, objetivos e destino do dinheiro, inflação, bancos digitais por geração, renda e canais",
    "Bloco 2 · 1.3.5 a 1.3.7": "Vantagens de investir, motivos para não investir, aposentadoria e fontes de renda",
    "Bloco 3 · 1.3.8 a 1.3.10": "Estresse financeiro, apostas online, educação financeira e finfluencers + questão 1",
    "Bloco 4 · 1.5": "Objetivos por prazo, liquidez, conhecimento, origem dos recursos e comprometimento da renda + questão 2",
    "Bloco 5 · 1.6.1": "Código ANBIMA de Distribuição: abrangência, regras gerais, KYC, suitability, perfis, produtos e transferência + questão 3",
    "Bloco 6 · 1.6.2 a 1.6.5": "CVM 30, CMN 4.949, BCB 155 e Res. Conjunta 8/2023 + questão 4",
    "Revisão": "Cinco ideias, quiz relâmpago, questão integradora e encerramento",
  };
  blocks.forEach((b) => out.push(`| ${b.name} | ${b.slides[0]}–${b.slides[b.slides.length - 1]} | ${fmt(b.time)} min | ${desc[b.name]} |`));
  out.push(`| **Total** | **${S.length}** | **${fmt(total)} min** | |`, "");
  out.push("**Interação prevista:** 4 perguntas rápidas (slides 3, 9, 22 e 39) e 5 questões autorais (slides 17, 23, 31, 37 e 40), com gabarito comentado nas notas.", "");
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
    "**Fontes conferidas (21–22/10/2026):**", "",
    "- Programa Detalhado C-PRO R (ANBIMA, v1.2, rev. 04/06/2025, vigência a partir de 01/01/2026), itens 1.3, 1.5 e 1.6.",
    "- Apostila C-PRO R (Top Invest, rev. mar/2026), p. 48–65, e slides X8 A5108 a A5112 e A5116 a A5124.",
    "- Raio X do Investidor Brasileiro, 9ª edição (ANBIMA/Datafolha, campo em novembro de 2025), PDF completo, e nota da ANBIMA de 12/05/2026 sobre bancos digitais.",
    "- Regras e Procedimentos do Código ANBIMA de Distribuição, versão de 13/05/2025 (PDF da ANBIMA): Caps. I, II, IV, V, VIII e X.",
    "- Resolução CVM 30/2021, texto consolidado (arts. 2º, 3º, 6º, 7º, 9º e 10).",
    "- Resolução BCB 155/2021 (escopo e vigência, via fonte secundária) e Resolução Conjunta nº 8/2023 (educação financeira; vigência via fonte secundária).",
    "- IPCA de setembro de 2026 (4,58% em 12 meses; imprensa citando o IBGE).",
    "- Caderno de Roteiros C-Pro R, aula 003 (casos Marlene, Aldenir, Rogério e Ubiratan; teto do INSS de 2026).", "",
    "**Correções em relação aos materiais de origem:**", "",
    "| Fonte | O material diz | O correto |",
    "| --- | --- | --- |",
    "| Slide X8 A5118-11 | Atualizar o perfil \"até 24 meses\" | Perfil: periodicidade do cadastro, **no máximo 5 anos** (CVM 30, art. 9º, I). **24 meses** é para a classificação dos **produtos** (art. 9º, II). As Regras ANBIMA mandam seguir o prazo da regulação |",
    "| PD 1.6.1.3 a 1.6.1.5.4 | KYC no Cap. III, suitability no Cap. IV, transferência no Cap. IX | Na versão de 13/05/2025: Caps. **IV, V e X** (foi incluído o capítulo de divulgação da remuneração). A aula ensina pelo tema |",
    "| Slides X8 A5118 a A5120 | Chamam o suitability de \"Capítulo V\" e o KYC de \"Capítulo IV\" | Coincide com a versão de 2025, mas diverge do PD; a fala explica a diferença |",
    "| PD 1.6.5 | \"Resolução conjunta BCB e CMN de 08/2023\" | É a **Resolução Conjunta nº 8, de 21/12/2023** (educação financeira): \"08\" é o número, não o mês |",
    "| Slide X8 A5124-5 | BCB 155 é \"a versão operacional da CMN 4.949\" | Mesmos princípios, **público diferente**: administradoras de consórcio e instituições de pagamento (e, após alterações, outras instituições autorizadas) |",
    "| Slide X8 A5109-6 | \"Quanto maior a renda, mais racional a decisão\" | Mais acesso a assessoria não elimina vieses; a classe AB tem a **maior incidência de golpes** (47%) |",
    "| Slide X8 A5111-7 | \"20 milhões já apostaram (IBOPE, 2024)\" | Usado o Raio X 9ª ed.: **17%** da população apostou em 2025 |",
    "| Caderno, aula 003 | \"Destino do dinheiro: imóvel 32%\" | 32% é o destino do **retorno** das aplicações; o destino do dinheiro economizado é aplicar 38%, guardar parado 19% |", "",
    "**Pendências:**", "",
    "- Teto do INSS de 2026 (R$ 8.475,55): vem do Caderno de Roteiros; reconferir na Portaria Interministerial MPS/MF nº 13/2026 antes de gravar.",
    "- Vigência da Res. Conjunta 8/2023 (01/07/2024) e escopo atualizado da BCB 155: confirmados só em fonte secundária.",
    "- Faixas de prazo dos objetivos (até 2 anos, 2 a 5, acima de 5) e reserva de 6 a 12 meses: convenção didática do material X8, não regra do PD.",
    "- Verificar se a ANBIMA publicou versão das Regras e Procedimentos posterior a 13/05/2025.", "");
  fs.writeFileSync(MD, out.join("\n"));
  console.log("ok", DECK, MD, "total", total, "slides", S.length);
})();
