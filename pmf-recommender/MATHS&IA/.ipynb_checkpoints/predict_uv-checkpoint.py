# predict_uv.py
from uv_model import UVRecommender

model = UVRecommender()
model.load("uv_model.pkl")

uid, iid = 100, 50
r_hat = model.predict(uid, iid)
print(f"Note prédite pour l'utilisateur {uid} et l'item {iid} : {r_hat:.2f}")