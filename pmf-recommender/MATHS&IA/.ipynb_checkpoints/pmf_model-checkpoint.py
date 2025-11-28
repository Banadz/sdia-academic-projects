import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

class PMFWithBias:
    def __init__(self, n_factors=10, lr=0.01, lambda_u=0.1, lambda_v=0.1,
                 lambda_bu=0.1, lambda_bi=0.1, lambda_rating=1.0, n_epochs=20):
        self.n_factors = n_factors
        self.lr = lr
        self.lambda_u = lambda_u
        self.lambda_v = lambda_v
        self.lambda_bu = lambda_bu
        self.lambda_bi = lambda_bi
        self.lambda_rating = lambda_rating
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
        self.bu = np.zeros(n_users)
        self.bi = np.zeros(n_items)

        train_data, val_data = train_test_split(df, test_size=0.2, random_state=42)

        for epoch in range(self.n_epochs):
            for _, row in train_data.iterrows():
                i_uid = self.user_map[row['user_id']]
                j_iid = self.item_map[row['item_id']]
                r = row['rating']

                pred = self.U[i_uid].dot(self.V[j_iid]) + self.bu[i_uid] + self.bi[j_iid]
                err = r - pred

                # Mises à jour par SGD
                self.U[i_uid] += self.lr * (self.lambda_rating * err * self.V[j_iid] - self.lambda_u * self.U[i_uid])
                self.V[j_iid] += self.lr * (self.lambda_rating * err * self.U[i_uid] - self.lambda_v * self.V[j_iid])
                self.bu[i_uid] += self.lr * (self.lambda_rating * err - self.lambda_bu * self.bu[i_uid])
                self.bi[j_iid] += self.lr * (self.lambda_rating * err - self.lambda_bi * self.bi[j_iid])

            rmse = self.evaluate(val_data)
            print(f"Epoch {epoch+1}/{self.n_epochs} - RMSE: {rmse:.4f}")

    def predict(self, user_id, item_id):
        if user_id in self.user_map and item_id in self.item_map:
            i_uid = self.user_map[user_id]
            j_iid = self.item_map[item_id]
            return self.U[i_uid].dot(self.V[j_iid]) + self.bu[i_uid] + self.bi[j_iid]
        else:
            return np.mean(self.U @ self.V.T)

    def evaluate(self, data):
        errors = []
        for _, row in data.iterrows():
            pred = self.predict(row['user_id'], row['item_id'])
            errors.append((row['rating'] - pred) ** 2)
        return np.sqrt(np.mean(errors))

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump((self.U, self.V, self.bu, self.bi, self.user_map, self.item_map), f)

    def load(self, path):
        with open(path, 'rb') as f:
            self.U, self.V, self.bu, self.bi, self.user_map, self.item_map = pickle.load(f)
