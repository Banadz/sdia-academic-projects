import pandas as pd
from pmf_model import PMFWithBias

df = pd.read_csv("data/ml-100k/u.data", sep="\t", names=["user_id", "item_id", "rating", "timestamp"])

model = PMFWithBias(n_factors=20, lr=0.005, lambda_u=0.1, lambda_v=0.1,
                    lambda_bu=0.05, lambda_bi=0.05, lambda_rating=1.0, n_epochs=20)
model.fit(df)

model.save("pmf_model.pkl")
