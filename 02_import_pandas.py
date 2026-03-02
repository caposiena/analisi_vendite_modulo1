import pandas as pd

# Importa CSV
df = pd.read_csv("vendite.csv")
df["Data"] = pd.to_datetime(df["Data"])  # converti Data in datetime

# Stampa richiesto
print("=== PRIME 5 RIGHE ===")
print(df.head())

print("\n=== SHAPE ===")
print("Righe:", df.shape[0], "Colonne:", df.shape[1])

print("\n=== INFO GENERALI ===")
print(df.info())
