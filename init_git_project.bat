@echo off
setlocal enabledelayedexpansion

echo.
echo === Inicializando repositorio Git en: %cd%
echo.

REM Verifica si ya es un repositorio
if exist ".git" (
    echo Ya existe un repositorio Git en este directorio.
    goto :end
)

REM Inicializa Git
git init

REM Configura nombre y correo si no están
for /f "tokens=* delims=" %%a in ('git config --global user.name') do set NAME=%%a
if not defined NAME (
    set /p NAME="Tu nombre para Git (user.name): "
    git config --global user.name "!NAME!"
)

for /f "tokens=* delims=" %%a in ('git config --global user.email') do set EMAIL=%%a
if not defined EMAIL (
    set /p EMAIL="Tu correo para Git (user.email): "
    git config --global user.email "!EMAIL!"
)

REM Crea .gitignore básico si no existe
if not exist ".gitignore" (
    echo __pycache__/>> .gitignore
    echo *.pyc>> .gitignore
    echo *.pyo>> .gitignore
    echo *.pyd>> .gitignore
    echo .Python>> .gitignore
    echo env/>> .gitignore
    echo .env/>> .gitignore
    echo .venv/>> .gitignore
    echo .vscode/>> .gitignore
    echo *.sqlite3>> .gitignore
    echo *.log>> .gitignore
    echo .DS_Store>> .gitignore
    echo Thumbs.db>> .gitignore
)

REM Rama main y commit inicial
git checkout -b main
git add .
git commit -m "Inicio de proyecto con estructura completa"

REM Opción para repositorio remoto
echo.
set /p REMOTE_URL="¿URL del repositorio remoto? (déjalo vacío para omitir): "
if NOT "%REMOTE_URL%"=="" (
    git remote add origin %REMOTE_URL%
    git push -u origin main
)

echo.
echo === Repositorio Git inicializado correctamente ===
echo.

:end
pause
endlocal
