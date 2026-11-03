@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  echo Rode primeiro o instalar_windows.bat
  pause
  exit /b 1
)
set PYTHONIOENCODING=utf-8
rem Arraste o video em cima deste arquivo. Nao transcreve: so mede.
rem O resultado aparece aqui e fica salvo em diagnostico.txt
.venv\Scripts\python transcrever.py --diagnostico %* > diagnostico.txt 2>&1
type diagnostico.txt
pause
