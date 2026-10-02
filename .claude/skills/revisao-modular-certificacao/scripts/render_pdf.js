// Renderiza o manual HTML em PDF A4 e checa se algum conteúdo invade o rodapé.
// Uso: NODE_PATH=$(npm root -g) node render_pdf.js <manual.html> <saida.pdf>
// Saída: uma linha por página com a folga (px) entre o conteúdo e o rodapé.
// Folga negativa = conteúdo encostando/invadindo o rodapé -> enxugar ou usar class="page tight".
const path = require('path');
const { chromium } = require('playwright');

(async () => {
  const [html, pdf] = process.argv.slice(2);
  if (!html || !pdf) { console.error('uso: node render_pdf.js <manual.html> <saida.pdf>'); process.exit(2); }
  const browser = await chromium.launch();
  const page = await browser.newPage();
  await page.goto('file://' + path.resolve(html), { waitUntil: 'networkidle' });
  await page.evaluate(() => document.fonts.ready);
  const gaps = await page.evaluate(() => [...document.querySelectorAll('.page')].map((p, i) => {
    const foot = p.querySelector('.foot');
    const limit = foot ? foot.getBoundingClientRect().top : p.getBoundingClientRect().bottom;
    let bottom = 0;
    [...p.children].forEach(c => {
      if (c.classList.contains('foot')) return;
      const r = c.getBoundingClientRect(); if (r.bottom > bottom) bottom = r.bottom;
    });
    return { page: i + 1, gap: Math.round(limit - bottom) };
  }));
  const fontOk = await page.evaluate(() => document.fonts.check('12px Poppins'));
  await page.pdf({ path: path.resolve(pdf), format: 'A4', printBackground: true, preferCSSPageSize: true });
  await browser.close();
  gaps.forEach(g => console.log(`página ${g.page}: folga ${g.gap}px${g.gap < 0 ? '  <-- TRANSBORDA' : ''}`));
  console.log(`fonte Poppins carregada: ${fontOk}`);
  const bad = gaps.filter(g => g.gap < 0);
  console.log(bad.length ? `ATENÇÃO: ${bad.length} página(s) transbordando` : 'OK: nenhuma página transbordando');
  process.exit(bad.length ? 1 : 0);
})();
