import pandas as pd
from bias_only_model import BiasOnlyRecommender
from uv_model import UVRecommender

# Charger le fichier u.data
df = pd.read_csv("data/ml-100k/u.data", sep="\t", names=["user_id", "item_id", "rating", "timestamp"])

# model = BiasOnlyRecommender(lr=0.005, lambda_user=0.1, lambda_item=0.1, n_epochs=15)
model = UVRecommender(n_factors=20, lr=0.01, lambda_u=0.1, lambda_v=0.1, n_epochs=20)

model.fit(df)

# Sauvegarde du modèle
# model.save("bias_model.pkl")
model.save("uv_model.pkl")