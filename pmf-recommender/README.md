# pmf-recommender

Projet portant sur la recommandation d'éléments via la factorisation matricielle probabiliste (PMF), axé sur les aspects mathématiques et l’apprentissage automatique appliqué.

## Architecture

- `MATHS&IA/`
    - `.ipynb_checkpoints/`, `.jupyter/` et `.venv/` : dossiers techniques liés à Jupyter et à l’environnement Python
    - `data/` : jeux de données pour l'entraînement et l’évaluation
    - Fichiers Python : 
        - `main.py`, `main_pmf.py` : scripts principaux d’exécution
        - `pmf_model.py`, `uv_model.py`, `bias_only_model.py` : implémentations des différents modèles de recommandation
        - `graph_learning.py` : apprentissage sur des structures de graphe
        - `predict.py`, `predict_pmf.py`, `predict_uv.py` : scripts de prédiction selon le modèle
    - Fichiers modèles sauvegardés : `pmf_model.pkl`, `uv_model.pkl`, `bias_model.pkl`
    - Documentation et résultats : `README.md`, `Comparaison des modèles.png`
    - `requierement.txt` : liste des principales dépendances

## Technologies

- Python 
- Utilisation de Jupyter Notebooks
- Probablement NumPy, Pandas, Matplotlib et bibliothèques de machine learning
- Sérialisation des modèles avec pickle (.pkl)
