@echo off
chcp 65001 >nul
cd /d "%~dp0"
if not exist .venv\Scripts\python.exe (
  echo Rode primeiro o instalar_windows.bat
  pause
  exit /b 1
)
set PYTHONIOENCODING=utf-8
rem Dica: arraste um video em cima deste arquivo para transcrever so ele.
.venv\Scripts\python transcrever.py %*
pause
