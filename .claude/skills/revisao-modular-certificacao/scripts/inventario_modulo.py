"""Inventário de um módulo para a revisão: itens do PD, aulas prontas e revisões já existentes.

Uso (a partir da raiz do repositório):
    python3 .claude/skills/revisao-modular-certificacao/scripts/inventario_modulo.py CPA 1

Imprime:
  1. todos os itens do módulo no PD, com o título juntado ao número (no PD.txt
     o número e o título às vezes ficam em linhas separadas);
  2. as aulas prontas (aulas/<cert>/aula-N.* e modelos/REFERENCIA-aula-<cert>-N.*)
     com os subitens da tabela "Checagem de escopo" de cada uma;
  3. revisões e manuais do módulo que já existem.
"""
import glob
import os
import re
import sys

cert, mod = sys.argv[1].upper(), sys.argv[2]
base = "aulas-certificacoes"
c = cert.lower()

# 1. Itens do PD
noise = re.compile(r"^(Programa detalhado|Data da elab|Vig[eê]ncia a partir|\d+)\s*$|^(Data da elab|Vig[eê]ncia)", re.I)
item = re.compile(r"^(\d+(?:\.\d+)+)\.\s*(.*)$")
lines = [l.strip() for l in open(f"{base}/00-fontes/programas-detalhados/PD-{cert}.txt", encoding="utf-8")]
lines = [l for l in lines if l and not noise.match(l)]
items, cur = [], None
for l in lines:
    m = item.match(l)
    if m:
        cur = [m.group(1), m.group(2)]
        items.append(cur)
    elif cur is not None and not cur[1].rstrip().endswith((".", ":")):
        cur[1] = (cur[1] + " " + l).strip()
mine = [(n, t) for n, t in items if n.split(".")[0] == mod]
print(f"== PD {cert} — módulo {mod}: {len(mine)} itens")
for n, t in mine:
    print(f"{'  ' * (n.count('.') - 1)}{n}  {t}")

# 2. Aulas prontas
print(f"\n== Aulas prontas (aulas/{c}/ e modelos/)")
files = sorted(glob.glob(f"{base}/aulas/{c}/aula-{mod}.*/aula.md")) + sorted(
    glob.glob(f"{base}/modelos/REFERENCIA-aula-{c}-{mod}.*.md"))
for f in files:
    txt = open(f, encoding="utf-8").read()
    sec = re.search(r"### Checagem de escopo\n(.*?)(?:\n### |\Z)", txt, re.S)
    subs = []
    if sec:
        for row in sec.group(1).splitlines():
            cols = [x.strip() for x in row.split("|")]
            if len(cols) > 2 and re.match(r"\d", cols[1]):
                code = cols[1].split(" ")[0]
                if code not in subs:
                    subs.append(code)
    print(f"- {os.path.relpath(f, base)}: {', '.join(subs) or '(sem tabela de escopo)'}")

# 3. Revisões existentes
print("\n== Revisões e manuais já existentes deste módulo")
found = sorted(glob.glob(f"{base}/roteiros/{c}/revisao-modulo-{mod}*")) + sorted(
    glob.glob(f"{base}/materiais/{c}/manual-revisao-modulo-{mod}*"))
print("\n".join(f"- {os.path.relpath(f, base)}" for f in found) or "- nenhuma")
