#!/bin/bash
cd "$(dirname "$0")" || exit 1
if [ ! -x .venv/bin/python ]; then
  echo "Rode primeiro o instalar_mac.command"
  read -n1 -r -p "Aperte uma tecla para fechar"; exit 1
fi
.venv/bin/python janela.py
