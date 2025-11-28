# uv_model.py
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

class UVRecommender:
    def __init__(self, n_factors=10, lr=0.01, lambda_u=0.1, lambda_v=0.1, n_epochs=20):
        self.n_factors = n_factors
        self.lr = lr
        self.lambda_u = lambda_u
        self.lambda_v = lambda_v
        self.n_epochs = n_epochs

    def fit(self, df):
        self.users = df['user_id'].unique()
        self.items = df['item_id'].unique()

        self.user_map = {uid: idx for idx, uid in enumerate(self.users)}
        self.item_map = {iid: idx for idx, iid in enumerate(self.items)}
        self.inv_user_map = {idx: uid for uid, idx in self.user_map.items()}
        self.inv_item_map = {idx: iid for iid, idx in self.item_map.items()}

        n_users = len(self.users)
        n_items = len(self.items)

        self.U = np.random.normal(scale=0.1, size=(n_users, self.n_factors))
        self.V = np.random.normal(scale=0.1, size=(n_items, self.n_factors))

        train_data, val_data = train_test_split(df, test_size=0.2, random_state=42)

        for epoch in range(self.n_epochs):
            for _, row in train_data.iterrows():
                u_id = self.user_map[row['user_id']]
                i_id = self.item_map[row['item_id']]
                r = row['rating']

                pred = self.U[u_id].dot(self.V[i_id])
                err = r - pred

                # Update
                self.U[u_id] += self.lr * (err * self.V[i_id] - self.lambda_u * self.U[u_id])
                self.V[i_id] += self.lr * (err * self.U[u_id] - self.lambda_v * self.V[i_id])

            rmse = self.evaluate(val_data)
            print(f"Epoch {epoch+1}/{self.n_epochs} - RMSE: {rmse:.4f}")

    def predict(self, user_id, item_id):
        if user_id in self.user_map and item_id in self.item_map:
            u_id = self.user_map[user_id]
            i_id = self.item_map[item_id]
            return self.U[u_id].dot(self.V[i_id])
        else:
            return np.mean(self.U @ self.V.T)  # fallback

    def evaluate(self, data):
        errors = []
        for _, row in data.iterrows():
            r_hat = self.predict(row['user_id'], row['item_id'])
            errors.append((row['rating'] - r_hat) ** 2)
        return np.sqrt(np.mean(errors))

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump((self.U, self.V, self.user_map, self.item_map), f)

    def load(self, path):
        with open(path, 'rb') as f:
            self.U, self.V, self.user_map, self.item_map = pickle.load(f)
