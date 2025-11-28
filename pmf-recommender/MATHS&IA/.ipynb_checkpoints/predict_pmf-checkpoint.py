from pmf_model import PMFWithBias

model = PMFWithBias()
model.load("pmf_model.pkl")

uid, iid = 100, 50
r_hat = model.predict(uid, iid)
print(f"Note prédite (PMF complet) pour user {uid} et item {iid} : {r_hat:.2f}")