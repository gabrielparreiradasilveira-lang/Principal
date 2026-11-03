@echo off
cd /d "%~dp0"
if not exist .venv\Scripts\pythonw.exe (
  echo Rode primeiro o instalar_windows.bat
  pause
  exit /b 1
)
rem Abre a janela sem a tela preta do terminal.
rem Se a janela nao abrir, o motivo fica em janela_erro.log
start "" .venv\Scripts\pythonw.exe janela.py
