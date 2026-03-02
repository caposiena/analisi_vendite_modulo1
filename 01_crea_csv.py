import pandas as pd
import numpy as np

np.random.seed(42)

date = pd.date_range("2023-09-01", periods=10, freq="D").strftime("%Y-%m-%d")
negozi = ["Milano", "Roma", "Napoli", "Torino", "Bari"]
prodotti = ["Smartphone", "Laptop", "TV", "Tablet", "Cuffie"]
prezzi = {"Smartphone": 499.99, "Laptop": 1099.00, "TV": 799.90, "Tablet": 329.00, "Cuffie": 89.90}

rows = []
for _ in range(35):
    rows.append([
        np.random.choice(date),
        np.random.choice(negozi),
        np.random.choice(prodotti),
        np.random.randint(1, 11),
        round(np.random.uniform(0.9, 1.1) * prezzi[np.random.choice(prodotti)], 2)
    ])

df = pd.DataFrame(rows, columns=["Data", "Negozio", "Prodotto", "Quantità", "Prezzo_unitario"])
df.to_csv("vendite.csv", index=False)
print("✓ vendite.csv creato:", len(df), "righe")
print(df.head())

