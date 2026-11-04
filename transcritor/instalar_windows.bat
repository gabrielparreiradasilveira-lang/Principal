@echo off
chcp 65001 >nul
cd /d "%~dp0"
echo Instalando o Transcritor...
echo.

rem 1) Escolhe o Python: prefere o 3.12 (lancador "py"); senao, o "python" do PATH.
set "PY="
py -3.12 -c "import sys" >nul 2>nul && set "PY=py -3.12"
if not defined PY (
  python -c "import sys" >nul 2>nul && set "PY=python"
)
if not defined PY (
  echo Python nao encontrado. Instale o Python 3.12 em python.org
  echo e marque a opcao "Add python.exe to PATH" na instalacao.
  pause
  exit /b 1
)
echo Python escolhido: %PY%

rem 2) Se o ambiente .venv ja existe mas nao funciona (ex.: criado com outro
rem    Python), apaga e refaz do zero. Os modelos baixados (pasta modelos) ficam.
if exist .venv\Scripts\python.exe (
  .venv\Scripts\python.exe -c "import numpy, ctranslate2, av, faster_whisper" >nul 2>nul
  if errorlevel 1 (
    echo Ambiente antigo incompativel. Apagando e refazendo do zero...
    rmdir /s /q .venv
    if exist .venv goto naoapagou
  )
)
if not exist .venv\Scripts\python.exe (
  %PY% -m venv .venv
  if errorlevel 1 goto erro
)

echo.
echo Instalando as bibliotecas (alguns minutos na primeira vez)...
.venv\Scripts\python.exe -m pip install --upgrade pip
.venv\Scripts\python.exe -m pip install -r requirements.txt
if errorlevel 1 goto erro

rem 3) Teste final: as bibliotecas precisam carregar de verdade.
.venv\Scripts\python.exe -c "import numpy, ctranslate2, av, faster_whisper; print('Teste final: OK')"
if errorlevel 1 goto erro
.venv\Scripts\python.exe -c "import tkinter" >nul 2>nul
if errorlevel 1 echo Aviso: este Python nao tem Tcl/Tk, entao a janela nao abre. Reinstale o Python marcando "tcl/tk and IDLE". O transcrever_windows.bat funciona mesmo assim.

echo.
echo Instalacao concluida. Agora use o abrir_janela_windows.bat
pause
exit /b 0

:naoapagou
echo.
echo Nao consegui apagar a pasta .venv porque ela esta em uso.
echo Feche a janela do Transcritor e rode este instalador de novo.
pause
exit /b 1

:erro
echo.
echo ERRO na instalacao. Copie as mensagens acima e envie para o suporte.
pause
exit /b 1
