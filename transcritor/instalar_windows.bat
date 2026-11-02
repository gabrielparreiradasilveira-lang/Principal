@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Instalando o Transcritor (so precisa fazer uma vez)...
where python >nul 2>nul || (
  echo Python nao encontrado. Instale o Python 3.12 em python.org
  echo e marque a opcao "Add python.exe to PATH" na instalacao.
  pause
  exit /b 1
)
python -m venv .venv || (pause & exit /b 1)
.venv\Scripts\python -m pip install --upgrade pip
.venv\Scripts\python -m pip install -r requirements.txt || (pause & exit /b 1)
echo.
echo Instalacao concluida. Agora use o arquivo transcrever_windows.bat
pause
