#!/bin/bash
cd "$(dirname "$0")" || exit 1
echo "Instalando o Transcritor..."
fechar() { read -n1 -r -p "Aperte uma tecla para fechar"; echo; exit "$1"; }

# 1) Python: prefere o 3.12; senão, o python3 do sistema
PY="$(command -v python3.12 || command -v python3)"
if [ -z "$PY" ]; then
  echo "Python 3 não encontrado. Instale o Python 3.12 em python.org"
  fechar 1
fi
echo "Python escolhido: $PY"

# 2) Se o ambiente .venv já existe mas não funciona (ex.: criado com outro
#    Python), apaga e refaz do zero. Os modelos baixados (pasta modelos) ficam.
TESTE="import numpy, ctranslate2, av, faster_whisper"
if [ -x .venv/bin/python ] && ! .venv/bin/python -c "$TESTE" 2>/dev/null; then
  echo "Ambiente antigo incompatível. Apagando e refazendo do zero..."
  rm -rf .venv
fi
if [ ! -x .venv/bin/python ]; then
  "$PY" -m venv .venv || { echo "ERRO ao criar o ambiente."; fechar 1; }
fi

echo "Instalando as bibliotecas (alguns minutos na primeira vez)..."
.venv/bin/python -m pip install --upgrade pip \
  && .venv/bin/python -m pip install -r requirements.txt \
  && .venv/bin/python -c "$TESTE; print('Teste final: OK')" \
  || { echo ""; echo "ERRO na instalação. Copie as mensagens acima e envie."; fechar 1; }
.venv/bin/python -c "import tkinter" 2>/dev/null \
  || echo "Aviso: este Python não tem Tkinter, então a janela não abre (o transcrever_mac.command funciona)."
echo ""
echo "Instalação concluída. Agora use o abrir_janela_mac.command"
fechar 0
