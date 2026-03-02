import pandas as pd

df = pd.read_csv("vendite.csv")
df["Data"] = pd.to_datetime(df["Data"])

# AGGIUNGI COLONNA INCASSO
df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]
print("Dataset con Incasso:")
print(df[["Data", "Negozio", "Prodotto", "Incasso"]].head())

# CALCOLI RICHIESTI
print("\n1. INCASSO TOTALE CATENA:")
print(df["Incasso"].sum())

print("\n2. INCASSO MEDIO PER NEGOZIO:")
print(df.groupby("Negozio")["Incasso"].mean().round(2))

print("\n3. TOP 3 PRODOTTI PER QUANTITÀ:")
print(df.groupby("Prodotto")["Quantità"].sum().sort_values(ascending=False).head(3))

print("\n4. INCASSO MEDIO PER NEGOZIO+PRODOTTO:")
print(df.groupby(["Negozio", "Prodotto"])["Incasso"].mean().round(2).head(10))
