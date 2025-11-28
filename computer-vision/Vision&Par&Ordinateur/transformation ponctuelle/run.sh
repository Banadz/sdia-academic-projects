#!/bin/bash

# Créer un environnement virtuel s’il n'existe pas
if [ ! -d "env" ]; then
    echo "📦 Création de l'environnement virtuel..."
    python3 -m venv env
fi

# Activer l'environnement virtuel
echo "🔁 Activation de l'environnement virtuel..."
source env/bin/activate

# Installer Pillow si nécessaire
pip show pillow > /dev/null 2>&1 || pip install pillow

# Lancer le programme
echo "🚀 Lancement de main.py"
python main.py

# Désactiver
deactivate
echo "✅ Script terminé avec succès."
