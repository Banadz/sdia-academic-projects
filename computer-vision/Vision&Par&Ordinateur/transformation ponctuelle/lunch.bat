@echo off
REM =============================
REM Script de lancement portable
REM =============================

REM Détection du système d'exploitation
ver | findstr /i "Windows" >nul
IF %ERRORLEVEL%==0 (
    echo ✅ Système détecté : Windows

    REM Vérifie si l'environnement virtuel existe
    IF NOT EXIST env (
        echo 🔧 Création de l'environnement virtuel...
        python -m venv env
    )

    REM Activation de l'environnement
    call env\Scripts\activate

    REM Installation de Pillow si nécessaire
    pip show pillow >nul 2>&1
    IF %ERRORLEVEL% NEQ 0 (
        echo 📦 Installation de Pillow...
        pip install pillow
    )

    echo 🚀 Lancement du script Python...
    python main.py

    REM Désactivation
    deactivate
    echo ✅ Terminé.
) ELSE (
    echo 🌍 Système détecté : Linux/macOS
    echo 🔁 Appel du script bash...

    REM Appel du script .sh via bash (si disponible)
    bash run.sh
)