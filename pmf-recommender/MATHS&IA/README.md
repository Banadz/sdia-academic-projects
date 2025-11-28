# 🎯 Probabilistic Matrix Factorization (PMF) – Recommender System

Ce projet implémente et compare trois variantes de modèles de recommandation basés sur la **factorisation matricielle probabiliste**, appliqués au jeu de données MovieLens 100k :

- ✅ Modèle 1 : biais uniquement
- ✅ Modèle 2 : vecteurs latents (U/V) uniquement
- ✅ Modèle 3 : modèle PMF complet (U/V + biais)

## 📁 Structure du projet

MATHS&IA/
├── data/ # Contient le jeu MovieLens 100k
├── graph_learning.py # Implémentation graphe de comparaison.
├── main.py # main pour le modèle 1 et modèle 2 
├── main_pmf.py # main pour le modèle 3
├── pmf_model.pkl
├── pmf_model.py
├── predict.py # script de prédiction pour le modèle 1
├── predict_pmf.py # script de prédiction pour le modèle 3
├── predict_uv.py # script de prédiction pour le modèle 2
├── requierement.txt
├── uv_model.pkl
└── uv_model.py



### 📁 Lancement du projet

Modèle biais uniquement et U/V uniquement: 
`python3 main.py`

Modèle complet: 
`python3 main_pmf.py`
