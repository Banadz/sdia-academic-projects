import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import pickle

class BiasOnlyRecommender:
    def __init__(self, lambda_user=0.1, lambda_item=0.1, lr=0.01, n_epochs=20):
        self.lambda_user = lambda_user
        self.lambda_item = lambda_item
        self.lr = lr
        self.n_epochs = n_epochs

    def fit(self, df):
        self.users = df['user_id'].unique()
        self.items = df['item_id'].unique()
        self.global_mean = df['rating'].mean()

        self.bu = {uid: 0.0 for uid in self.users}
        self.bi = {iid: 0.0 for iid in self.items}

        train_data, val_data = train_test_split(df, test_size=0.2, random_state=42)

        for epoch in range(self.n_epochs):
            for _, row in train_data.iterrows():
                u, i, r = row['user_id'], row['item_id'], row['rating']

                pred = self.global_mean + self.bu[u] + self.bi[i]
                err = r - pred

                self.bu[u] += self.lr * (err - self.lambda_user * self.bu[u])
                self.bi[i] += self.lr * (err - self.lambda_item * self.bi[i])

            rmse = self.evaluate(val_data)
            print(f"Epoch {epoch+1}/{self.n_epochs} - RMSE: {rmse:.4f}")

    def predict(self, user_id, item_id):
        return self.global_mean + self.bu.get(user_id, 0.0) + self.bi.get(item_id, 0.0)

    def evaluate(self, data):
        errors = []
        for _, row in data.iterrows():
            u, i, r = row['user_id'], row['item_id'], row['rating']
            pred = self.predict(u, i)
            errors.append((r - pred) ** 2)
        return np.sqrt(np.mean(errors))

    def save(self, path):
        with open(path, 'wb') as f:
            pickle.dump((self.global_mean, self.bu, self.bi), f)

    def load(self, path):
        with open(path, 'rb') as f:
            self.global_mean, self.bu, self.bi = pickle.load(f)
