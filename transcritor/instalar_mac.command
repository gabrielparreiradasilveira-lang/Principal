#!/bin/bash
cd "$(dirname "$0")" || exit 1
echo "Instalando o Transcritor (só precisa fazer uma vez)..."
if ! command -v python3 >/dev/null; then
  echo "Python 3 não encontrado. Instale o Python 3.12 em python.org"
  read -n1 -r -p "Aperte uma tecla para fechar"; exit 1
fi
python3 -m venv .venv \
  && .venv/bin/python -m pip install --upgrade pip \
  && .venv/bin/python -m pip install -r requirements.txt \
  && echo "" && echo "Instalação concluída. Agora use o transcrever_mac.command"
read -n1 -r -p "Aperte uma tecla para fechar"
