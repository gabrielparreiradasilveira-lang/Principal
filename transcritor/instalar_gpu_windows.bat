@echo off
chcp 65001 >nul
cd /d "%~dp0"
set PYTHONIOENCODING=utf-8
if not exist .venv\Scripts\python.exe (
  echo Rode primeiro o instalar_windows.bat
  pause
  exit /b 1
)
echo Instalando as bibliotecas da NVIDIA para usar a placa de video.
echo Sao cerca de 1,3 GB e so precisa fazer uma vez.
echo.
.venv\Scripts\python.exe -m pip install "nvidia-cublas-cu12>=12,<13" "nvidia-cudnn-cu12>=9,<10"
if errorlevel 1 goto erro
echo.
echo Testando a placa de video...
.venv\Scripts\python.exe transcrever.py --testar-gpu
if errorlevel 1 goto erro
echo.
echo Pronto: as proximas transcricoes vao usar a placa de video.
pause
exit /b 0

:erro
echo.
echo Algo deu errado. Copie as mensagens acima e envie para o suporte.
echo Enquanto isso, o transcritor continua funcionando pela CPU.
pause
exit /b 1
