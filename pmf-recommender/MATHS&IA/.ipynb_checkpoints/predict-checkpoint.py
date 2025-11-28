# predict.py
from bias_only_model import BiasOnlyRecommender

model = BiasOnlyRecommender()
model.load("bias_model.pkl")

# Exemple : prédire la note de l'utilisateur 100 sur l'item 50
pred = model.predict(100, 50)
print(f"Note prédite : {pred:.2f}")
