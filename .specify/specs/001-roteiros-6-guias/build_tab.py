#!/usr/bin/env python3
"""Converte um roteiro em MD (dialeto do plano 001) em requests do Google Docs para uma guia.

Uso: build_tab.py ARQ.md --tab TAB_ID [--out requests.json]

Dialeto: '#'..'####' títulos; '- ' marcador (nível 1); '  - ' fala (nível 2);
'1. ' lista numerada; '> ' frase de fixação; linhas '|' = tabela (1ª linha = cabeçalho);
demais linhas = parágrafo. Inline: **negrito**, *itálico*.

Supõe guia nova (um parágrafo vazio, índice 1). Inserções em ordem crescente;
estilos depois; bullets por último, do maior índice para o menor.
"""
import argparse, json, re

HEAD = {'#': 'HEADING_1', '##': 'HEADING_2', '###': 'HEADING_3', '####': 'HEADING_4'}


def u16(s):
    return len(s.encode('utf-16-le')) // 2


def inline(s):
    """Retorna (texto_limpo, [(ini, fim, 'bold'|'italic')]) em unidades UTF-16."""
    out, spans, pos = [], [], 0
    for tok in re.split(r'(\*\*[^*]+\*\*|\*[^*\s][^*]*\*)', s):
        if not tok:
            continue
        if tok.startswith('**') and tok.endswith('**') and len(tok) > 4:
            t, kind = tok[2:-2], 'bold'
        elif tok.startswith('*') and tok.endswith('*') and len(tok) > 2:
            t, kind = tok[1:-1], 'italic'
        else:
            t, kind = tok, None
        if kind:
            spans.append((pos, pos + u16(t), kind))
        out.append(t)
        pos += u16(t)
    return ''.join(out), spans


def parse(md):
    blocks, lines, i = [], md.split('\n'), 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip() or ln.strip() == '---':
            i += 1
            continue
        if ln.lstrip().startswith('|'):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith('|'):
                cells = [c.strip() for c in lines[i].strip().strip('|').split('|')]
                if not all(re.fullmatch(r':?-{2,}:?', c) for c in cells):
                    rows.append(cells)
                i += 1
            blocks.append(('table', rows))
            continue
        m = re.match(r'^(#{1,4}) (.*)$', ln)
        if m:
            blocks.append(('head', HEAD[m.group(1)], m.group(2)))
        elif re.match(r'^  +- ', ln):
            blocks.append(('li', 1, ln.strip()[2:]))
        elif ln.startswith('- '):
            blocks.append(('li', 0, ln[2:]))
        elif re.match(r'^\d+\. ', ln):
            blocks.append(('ol', 0, re.sub(r'^\d+\. ', '', ln)))
        elif ln.startswith('> '):
            blocks.append(('quote', ln[2:]))
        else:
            blocks.append(('p', ln.strip()))
        i += 1
    return blocks


def build(md, tab):
    loc = lambda idx: {'index': idx, 'tabId': tab}
    rng = lambda a, b: {'startIndex': a, 'endIndex': b, 'tabId': tab}
    ins, styles, bullets = [], [], []
    cur = 1
    paras = []          # (start, end, namedStyle, kind)
    text_spans = []     # (start, end, kind)
    plain_ranges = []   # ranges to reset bold/italic
    lists = []          # current list run: [kind, start, end]
    run = None
    for b in parse(md):
        if b[0] == 'table':
            run = None
            rows = b[1]
            R, C = len(rows), max(len(r) for r in rows)
            rows = [r + [''] * (C - len(r)) for r in rows]
            i = cur - 1
            ins.append({'insertTable': {'rows': R, 'columns': C, 'location': loc(i)}})
            cells, offset = [], 0
            for r in range(R):
                for c in range(C):
                    t, sp = inline(rows[r][c])
                    base = i + 4 + r * (2 * C + 1) + 2 * c
                    cells.append((base, t, sp, r))
            for base, t, sp, r in reversed(cells):
                if t:
                    ins.append({'insertText': {'text': t, 'location': loc(base)}})
            for base, t, sp, r in cells:
                a = base + offset
                if t:
                    plain_ranges.append((a, a + u16(t)))
                    if r == 0:
                        text_spans.append((a, a + u16(t), 'bold'))
                    for s, e, k in sp:
                        text_spans.append((a + s, a + e, k))
                offset += u16(t)
            cur = i + 3 + R * (2 * C + 1) + offset
            continue
        kind = b[0]
        if kind == 'head':
            style, raw = b[1], b[2]
        elif kind in ('li', 'ol'):
            style, raw = 'NORMAL_TEXT', b[2]
        else:
            style, raw = 'NORMAL_TEXT', b[1]
        t, sp = inline(raw)
        lead = '\t' if kind == 'li' and b[1] == 1 else ''
        full = lead + t + '\n'
        ins.append({'insertText': {'text': full, 'location': loc(cur)}})
        a = cur + u16(lead)
        e = a + u16(t)
        paras.append((cur, cur + u16(full), style, kind))
        if kind != 'head':
            plain_ranges.append((a, e))
        if kind == 'quote':
            text_spans.append((a, e, 'bold'))
        for s, f, k in sp:
            text_spans.append((a + s, a + f, k))
        if kind in ('li', 'ol'):
            lk = 'ol' if kind == 'ol' else 'li'
            if run and run[0] == lk and run[2] == cur:
                run[2] = cur + u16(full)
            else:
                run = [lk, cur, cur + u16(full)]
                lists.append(run)
        else:
            run = None
        cur += u16(full)
    merged = []
    for s, e, st, kind in paras:
        if merged and merged[-1][1] == s and merged[-1][2] == st and kind != 'quote' and merged[-1][3] != 'quote' and not st.startswith('HEADING'):
            merged[-1][1] = e
        else:
            merged.append([s, e, st, kind])
    for s, e, st, kind in merged:
        ps = {'namedStyleType': st}
        fields = 'namedStyleType'
        if kind == 'quote':
            ps.update({'indentStart': {'magnitude': 18, 'unit': 'PT'},
                       'shading': {'backgroundColor': {'color': {'rgbColor': {'red': 0.93, 'green': 0.95, 'blue': 1}}}}})
            fields += ',indentStart,shading'
        if st.startswith('HEADING'):
            ps['keepWithNext'] = True
            fields += ',keepWithNext'
        styles.append({'updateParagraphStyle': {'range': rng(s, e), 'paragraphStyle': ps, 'fields': fields}})
    styles.append({'updateTextStyle': {'range': rng(1, cur), 'textStyle': {}, 'fields': 'bold,italic'}})
    for a, e, k in text_spans:
        if e > a:
            styles.append({'updateTextStyle': {'range': rng(a, e), 'textStyle': {k: True}, 'fields': k}})
    for lk, s, e in sorted(lists, key=lambda x: -x[1]):
        preset = 'NUMBERED_DECIMAL_ALPHA_ROMAN' if lk == 'ol' else 'BULLET_DISC_CIRCLE_SQUARE'
        bullets.append({'createParagraphBullets': {'range': rng(s, e), 'bulletPreset': preset}})
    ntabs = sum(1 for b in parse(md) if b[0] == 'li' and b[1] == 1)
    ntables = sum(1 for b in parse(md) if b[0] == 'table')
    end = cur - ntabs
    if ntables:
        bullets.append({'deleteContentRange': {'range': rng(end, end + ntables)}})
    merged_ins = []
    for r in ins:
        t = r.get('insertText')
        if t and merged_ins and 'insertText' in merged_ins[-1]:
            prev = merged_ins[-1]['insertText']
            if prev['location']['index'] + u16(prev['text']) == t['location']['index'] and prev['text'].endswith('\n'):
                prev['text'] += t['text']
                continue
        merged_ins.append(r)
    return merged_ins + styles + bullets


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument('md')
    ap.add_argument('--tab', required=True)
    ap.add_argument('--out')
    a = ap.parse_args()
    req = build(open(a.md, encoding='utf-8').read(), a.tab)
    s = json.dumps(req, ensure_ascii=False, separators=(',', ':'))
    if a.out:
        open(a.out, 'w', encoding='utf-8').write(s)
    print(len(req), 'requests', len(s), 'chars')
