// Componentes visuais no padrão X8 (extraídos do deck de referência da Aula 1).
const pptxgen = require("pptxgenjs");

const THEME = {
  name: "X8 Educacao",
  headFontFace: "Cambria",
  bodyFontFace: "Calibri",
  colors: {
    dk1: "0A1628", lt1: "FFFFFF", dk2: "102040", lt2: "E8EDF5",
    accent1: "3B82F6", accent2: "C9A45C", accent3: "CADCFC", accent4: "94A3B8",
    accent5: "2563EB", accent6: "1C3260", hlink: "3B82F6", folHlink: "CADCFC",
  },
};

function makeDeck(opts) {
  const pres = new pptxgen();
  pres.layout = "LAYOUT_16x9";
  pres.author = "X8 Educação";
  pres.title = opts.title;
  pres.theme = { headFontFace: THEME.headFontFace, bodyFontFace: THEME.bodyFontFace };
  const C = pres.SchemeColor;

  pres.defineSlideMaster({
    title: "X8_CAPA",
    background: { color: "071020" },
    objects: [{ image: { path: opts.logo, x: 7.35, y: 1.25, w: 2.0, h: 2.0 } }],
    slideNumber: { x: 9.2, y: 5.22, w: 0.5, h: 0.25, fontSize: 9, color: C.accent4, align: "right" },
  });
  pres.defineSlideMaster({
    title: "X8_CONTEUDO",
    background: { color: "0A1628" },
    objects: [
      { image: { path: opts.logo, x: 9.08, y: 0.18, w: 0.62, h: 0.62 } },
      { text: { text: opts.footer, options: { x: 0.5, y: 5.22, w: 5.0, h: 0.25, fontSize: 9, color: C.accent4, charSpacing: 2, margin: 0 } } },
      { placeholder: { options: { name: "title", type: "title", x: 0.5, y: 0.5, w: 8.4, h: 0.62, fontFace: "Cambria", fontSize: 24, bold: true, color: C.background1, align: "left", valign: "middle", margin: 0 }, text: "" } },
    ],
    slideNumber: { x: 9.2, y: 5.22, w: 0.5, h: 0.25, fontSize: 9, color: C.accent4, align: "right" },
  });
  return { pres, C };
}

// ---------- primitivas ----------
function T(slide, text, o) {
  slide.addText(text, Object.assign({ isTextBox: true, margin: 0, valign: "top", fontFace: "Calibri" }, o));
}
function card(slide, C, x, y, w, h, o = {}) {
  const hi = o.hi;
  slide.addShape("roundRect", {
    x, y, w, h, rectRadius: o.r ?? 0.07,
    fill: { color: hi ? C.accent5 : C.text2 },
    line: { color: o.line ?? C.accent6, width: o.lw ?? 0.75 },
    shadow: o.noShadow ? undefined : { type: "outer", blur: 8, offset: 2, angle: 90, color: "000000", opacity: 0.35 },
    objectName: o.name || "card",
  });
}
function circle(slide, C, x, y, d, label, o = {}) {
  const fill = o.inv ? C.background1 : (o.gold ? C.accent2 : (o.fill || C.accent1));
  slide.addShape("ellipse", { x, y, w: d, h: d, fill: { color: fill }, line: { color: fill, width: 1 }, objectName: "marcador" });
  T(slide, label, { x, y, w: d, h: d, fontFace: "Cambria", fontSize: o.fs || 11, bold: true, color: o.inv ? C.accent5 : (o.gold ? C.text1 : C.background1), align: "center", valign: "middle" });
}
function tag(slide, C, text) {
  T(slide, text, { x: 0.5, y: 0.24, w: 7.5, h: 0.25, fontSize: 10, bold: true, color: C.accent1, charSpacing: 3 });
}
function head(pres, C, s) {
  const slide = pres.addSlide({ masterName: "X8_CONTEUDO", sectionTitle: s.section });
  tag(slide, C, s.tag);
  slide.addText(s.title, { placeholder: "title" });
  return slide;
}
function band(slide, C, text, y = 4.3, h = 0.6) {
  slide.addShape("roundRect", { x: 0.5, y, w: 9.0, h, rectRadius: 0.08, fill: { color: C.text2 }, line: { color: C.accent2, width: 0.75 }, objectName: "na-prova" });
  T(slide, "NA PROVA", { x: 0.72, y, w: 1.2, h, fontSize: 11, bold: true, color: C.accent2, charSpacing: 2, valign: "middle" });
  T(slide, text, { x: 1.9, y, w: 7.45, h, fontSize: 12.5, color: C.background2, valign: "middle" });
}
function bullets(items, C, fs = 13.5) {
  return items.map((t, i) => ({ text: t, options: { bullet: { indent: 14 }, color: C.background2, fontSize: fs, paraSpaceAfter: 4, breakLine: i < items.length - 1 } }));
}

// ---------- tipos de slide ----------
const R = {};

R.capa = (pres, C, s) => {
  const slide = pres.addSlide({ masterName: "X8_CAPA", sectionTitle: s.section });
  T(slide, s.kicker, { x: 0.6, y: 1.05, w: 6.2, h: 0.3, fontSize: 12, bold: true, color: C.accent2, charSpacing: 4 });
  T(slide, s.title, { x: 0.6, y: 1.45, w: 6.4, h: 1.6, fontFace: "Cambria", fontSize: s.titleSize || 32, bold: true, color: C.background1 });
  if (s.sub) T(slide, s.sub, { x: 0.6, y: 3.2, w: 6.2, h: 0.75, fontSize: 15, color: C.accent3 });
  T(slide, s.sign, { x: 0.6, y: 4.55, w: 6.0, h: 0.35, fontFace: "Cambria", fontSize: 14, italic: true, color: C.accent2 });
  return slide;
};

// cartões numerados em sequência, com chevrons (2, 3 ou 4 colunas)
R.flow = (pres, C, s) => {
  const slide = head(pres, C, s);
  let y = 1.4;
  if (s.case) {
    card(slide, C, 0.5, 1.3, 9.0, 0.78, { noShadow: true });
    T(slide, s.case, { x: 0.72, y: 1.3, w: 8.6, h: 0.78, fontSize: 13.5, color: C.background1, valign: "middle" });
    y = 2.25;
  }
  const n = s.cards.length, gap = 0.32, w = (9.0 - gap * (n - 1)) / n;
  const h = s.h || (s.band ? (s.case ? 1.85 : 2.65) : 2.75);
  s.cards.forEach((c, i) => {
    const x = 0.5 + i * (w + gap), hi = c.hi || (s.hiLast && i === n - 1);
    card(slide, C, x, y, w, h, { hi });
    circle(slide, C, x + 0.2, y + 0.18, 0.4, c.n || String(i + 1).padStart(2, "0"), { inv: hi });
    T(slide, c.t, { x: x + 0.2, y: y + 0.66, w: w - 0.3, h: 0.6, fontFace: "Cambria", fontSize: n === 4 ? 13.5 : 15, bold: true, color: C.background1 });
    T(slide, c.d, { x: x + 0.2, y: y + 1.3, w: w - 0.35, h: h - 1.38, fontSize: n === 4 ? 12 : 13, color: hi ? C.background1 : C.accent3 });
    if (i < n - 1 && !s.noArrows) slide.addShape("chevron", { x: x + w + 0.07, y: y + h / 2 - 0.12, w: 0.18, h: 0.24, fill: { color: C.accent2 }, line: { color: C.accent2, width: 1 }, objectName: "seta" });
  });
  if (s.foot) T(slide, s.foot, { x: 0.5, y: y + h + 0.18, w: 9.0, h: 0.45, fontSize: 13, italic: true, color: C.accent4 });
  if (s.band) band(slide, C, s.band, 4.3, 0.6);
  return slide;
};

// duas colunas com "x" central
R.compare = (pres, C, s) => {
  const slide = head(pres, C, s);
  let y = 1.35;
  if (s.lead) { T(slide, s.lead, { x: 0.5, y: 1.25, w: 9.0, h: 0.35, fontSize: 13.5, color: C.accent3 }); y = 1.7; }
  const h = (s.band ? 4.15 : 4.85) - y;
  [s.left, s.right].forEach((col, i) => {
    const x = i === 0 ? 0.5 : 5.15;
    card(slide, C, x, y, 4.35, h, { hi: col.hi });
    T(slide, col.t, { x: x + 0.25, y: y + 0.17, w: 3.85, h: 0.4, fontFace: "Cambria", fontSize: 15.5, bold: true, color: col.hi ? C.background1 : (i === 0 ? C.accent3 : C.accent2) });
    slide.addText(bullets(col.items, C, s.fs || 13.5), { x: x + 0.25, y: y + 0.65, w: 3.85, h: h - 0.8, valign: "top", margin: 0, fontFace: "Calibri" });
  });
  circle(slide, C, 4.69, y + h / 2 - 0.21, 0.42, s.mid || "x", { fill: C.accent5, fs: 14 });
  if (s.band) band(slide, C, s.band, 4.3, 0.6);
  return slide;
};

// conceito: O QUE É | NA FALA DO CLIENTE | COMO AGIR | NA PROVA
R.concept = (pres, C, s) => {
  const slide = head(pres, C, s);
  card(slide, C, 0.5, 1.35, 4.2, 2.6);
  T(slide, s.l1 || "O QUE É", { x: 0.72, y: 1.52, w: 3.8, h: 0.25, fontSize: 10, bold: true, color: C.accent1, charSpacing: 3 });
  T(slide, s.what, { x: 0.72, y: 1.85, w: 3.8, h: 2.0, fontSize: s.wfs || 14, color: C.background1 });
  slide.addShape("roundRect", { x: 4.95, y: 1.35, w: 4.55, h: 1.25, rectRadius: 0.08, fill: { color: C.text2 }, line: { color: C.accent2, width: 1 }, objectName: "fala" });
  T(slide, s.l2 || "NA FALA DO CLIENTE", { x: 5.17, y: 1.47, w: 4.1, h: 0.22, fontSize: 10, bold: true, color: C.accent2, charSpacing: 3 });
  T(slide, s.say, { x: 5.17, y: 1.72, w: 4.15, h: 0.8, fontSize: 13.5, italic: true, color: C.background1, valign: "middle" });
  card(slide, C, 4.95, 2.72, 4.55, 1.23, { hi: true });
  T(slide, s.l3 || "COMO AGIR", { x: 5.17, y: 2.83, w: 4.1, h: 0.22, fontSize: 10, bold: true, color: C.accent3, charSpacing: 3 });
  T(slide, s.act, { x: 5.17, y: 3.08, w: 4.15, h: 0.82, fontSize: 13, color: C.background1 });
  if (s.band) band(slide, C, s.band, 4.15, 0.6);
  return slide;
};

// diálogo em balões
R.dialog = (pres, C, s) => {
  const slide = head(pres, C, s);
  const n = s.lines.length, bh = s.bh || 0.62, gap = s.gap || 0.12;
  s.lines.forEach((l, i) => {
    const pro = l.who === "PROFISSIONAL", x = pro ? 3.1 : 0.5, y = 1.32 + i * (bh + gap);
    slide.addShape("roundRect", { x, y, w: 6.4, h: bh, rectRadius: 0.12, fill: { color: pro ? C.accent5 : C.text2 }, line: { color: pro ? C.accent5 : C.accent6, width: 0.75 }, objectName: "balao" });
    slide.addText([
      { text: l.who + "   ", options: { fontSize: 10, bold: true, color: pro ? C.accent3 : C.accent2, charSpacing: 2 } },
      { text: l.t, options: { fontSize: 13.5, color: C.background1 } },
    ], { x: x + 0.22, y, w: 5.96, h: bh, valign: "middle", margin: 0, fontFace: "Calibri" });
  });
  const yb = 1.32 + n * (bh + gap) + 0.08;
  if (s.defs) {
    s.defs.forEach((d, i) => {
      const x = i === 0 ? 0.5 : 5.1;
      slide.addShape("roundRect", { x, y: yb, w: 4.4, h: 4.85 - yb, rectRadius: 0.08, fill: { color: C.text2 }, line: { color: C.accent6, width: 0.75 }, objectName: "definicao" });
      slide.addText([
        { text: d.k + "   ", options: { bold: true, color: i === 0 ? C.accent2 : C.accent3, fontSize: 13 } },
        { text: d.v, options: { color: C.background2, fontSize: 12.5 } },
      ], { x: x + 0.2, y: yb, w: 4.0, h: 4.85 - yb, valign: "middle", margin: 0, fontFace: "Calibri" });
    });
  }
  if (s.band) band(slide, C, s.band, 4.3, 0.6);
  return slide;
};

// cartões de números grandes (2 ou 3)
R.stats = (pres, C, s) => {
  const slide = head(pres, C, s);
  let y = 1.35;
  if (s.case) {
    card(slide, C, 0.5, 1.28, 9.0, 0.7, { noShadow: true });
    T(slide, s.case, { x: 0.72, y: 1.28, w: 8.6, h: 0.7, fontSize: 13.5, color: C.background1, valign: "middle" });
    y = 2.12;
  }
  const n = s.cards.length, gap = 0.24, w = (9.0 - gap * (n - 1)) / n, h = (s.band ? 4.0 : 4.75) - y;
  s.cards.forEach((c, i) => {
    const x = 0.5 + i * (w + gap), hi = c.hi;
    card(slide, C, x, y, w, h, { hi });
    T(slide, c.k, { x: x + 0.22, y: y + 0.15, w: w - 0.4, h: 0.25, fontSize: 10, bold: true, color: C.accent3, charSpacing: 2 });
    if (c.line) T(slide, c.line, { x: x + 0.22, y: y + 0.45, w: w - 0.4, h: 0.35, fontSize: 13, color: C.background1 });
    T(slide, c.big, { x: x + 0.22, y: y + (c.line ? 0.82 : 0.5), w: w - 0.4, h: 0.85, fontFace: "Cambria", fontSize: c.bfs || 40, bold: true, color: hi ? C.background1 : C.accent2 });
    T(slide, c.sub, { x: x + 0.22, y: y + (c.line ? 1.68 : 1.4), w: w - 0.4, h: h - (c.line ? 1.75 : 1.5), fontSize: 12.5, color: C.accent3 });
  });
  if (s.band) band(slide, C, s.band, 4.15, 0.62);
  return slide;
};

// grade de cartões numerados (2x2 ou 3x2)
R.grid = (pres, C, s) => {
  const slide = head(pres, C, s);
  const cols = s.cols || 3, rows = Math.ceil(s.cards.length / cols), gap = 0.25;
  const top = s.lead ? 1.72 : 1.35, bottom = s.band ? 4.12 : 4.88;
  if (s.lead) T(slide, s.lead, { x: 0.5, y: 1.25, w: 9.0, h: 0.35, fontSize: 13.5, color: C.accent3 });
  const w = (9.0 - gap * (cols - 1)) / cols, h = (bottom - top - gap * (rows - 1)) / rows;
  s.cards.forEach((c, i) => {
    const x = 0.5 + (i % cols) * (w + gap), y = top + Math.floor(i / cols) * (h + gap), hi = c.hi;
    card(slide, C, x, y, w, h, { hi });
    circle(slide, C, x + 0.18, y + 0.15, 0.36, c.n || String(i + 1), { inv: hi, fs: 10.5 });
    T(slide, c.t, { x: x + 0.66, y: y + 0.12, w: w - 0.8, h: 0.42, fontFace: "Cambria", fontSize: 14, bold: true, color: C.background1, valign: "middle" });
    T(slide, c.d, { x: x + 0.18, y: y + 0.6, w: w - 0.34, h: h - 0.66, fontSize: s.dfs || 12, color: hi ? C.background1 : C.accent3 });
  });
  if (s.band) band(slide, C, s.band, 4.3, 0.6);
  return slide;
};

// tabela
R.table = (pres, C, s) => {
  const slide = head(pres, C, s);
  const fs = s.fs || 12;
  const rows = [s.cols.map((h) => ({ text: h, options: { bold: true, color: C.background1, fill: { color: C.accent5 }, fontSize: fs } }))];
  s.rows.forEach((r, i) => rows.push(r.map((c, j) => ({ text: c, options: { bold: j === 0, color: j === 0 ? C.background1 : C.background2, fill: { color: i % 2 ? C.accent6 : C.text2 }, fontSize: fs } }))));
  const y = s.lead ? 1.72 : 1.35;
  if (s.lead) T(slide, s.lead, { x: 0.5, y: 1.25, w: 9.0, h: 0.35, fontSize: 13.5, color: C.accent3 });
  slide.addTable(rows, { x: 0.5, y, w: 9.0, colW: s.colW, rowH: s.rowH || 0.42, border: { type: "solid", pt: 0.75, color: "1C3260" }, fontFace: "Calibri", valign: "middle", margin: [3, 7, 3, 7] });
  if (s.band) band(slide, C, s.band, 4.3, 0.6);
  return slide;
};

// questão autoral: caso + comando + 4 alternativas
R.question = (pres, C, s) => {
  const slide = head(pres, C, s);
  const ch = s.ch || 1.0;
  card(slide, C, 0.5, 1.3, 9.0, ch, { noShadow: true });
  T(slide, s.case, { x: 0.72, y: 1.3, w: 8.6, h: ch, fontSize: s.cfs || 13, color: C.background2, valign: "middle" });
  const yq = 1.3 + ch + 0.1;
  T(slide, s.ask, { x: 0.5, y: yq, w: 9.0, h: 0.38, fontSize: 13.5, bold: true, color: C.background1, valign: "middle" });
  const y0 = yq + 0.48, ah = s.ah || 0.7, aw = 4.43;
  s.alts.forEach((a, i) => {
    const x = i % 2 ? 5.07 : 0.5, y = y0 + Math.floor(i / 2) * (ah + 0.12);
    slide.addShape("roundRect", { x, y, w: aw, h: ah, rectRadius: 0.08, fill: { color: C.text2 }, line: { color: C.accent6, width: 0.75 }, objectName: "alternativa" });
    circle(slide, C, x + 0.14, y + ah / 2 - 0.18, 0.36, "ABCD"[i], { fill: C.accent5, fs: 12 });
    T(slide, a, { x: x + 0.62, y, w: aw - 0.74, h: ah, fontSize: s.afs || 12, color: C.background1, valign: "middle" });
  });
  return slide;
};

// lista numerada (revisão)
R.review = (pres, C, s) => {
  const slide = head(pres, C, s);
  s.items.forEach((t, i) => {
    const y = 1.32 + i * 0.75;
    circle(slide, C, 0.5, y + 0.07, 0.5, String(i + 1).padStart(2, "0"), { fill: i === s.items.length - 1 ? undefined : C.accent5, gold: i === s.items.length - 1, fs: 13 });
    T(slide, t, { x: 1.2, y, w: 8.3, h: 0.64, fontSize: 14.5, color: C.background1, valign: "middle" });
  });
  return slide;
};

// quatro frases numeradas (quiz)
R.quiz = (pres, C, s) => {
  const slide = head(pres, C, s);
  s.items.forEach((t, i) => {
    const x = i % 2 ? 5.15 : 0.5, y = 1.32 + Math.floor(i / 2) * 1.45;
    card(slide, C, x, y, 4.35, 1.28, { noShadow: true });
    circle(slide, C, x + 0.18, y + 0.15, 0.34, String(i + 1), { fs: 10.5 });
    T(slide, t, { x: x + 0.2, y: y + 0.52, w: 3.95, h: 0.7, fontSize: 13.5, color: C.background1 });
  });
  T(slide, s.foot, { x: 0.5, y: 4.3, w: 9.0, h: 0.42, fontSize: 13.5, bold: true, color: C.accent2 });
  return slide;
};

module.exports = { THEME, makeDeck, R };
