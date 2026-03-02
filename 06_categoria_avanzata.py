import pandas as pd

df = pd.read_csv("vendite.csv")
df["Data"] = pd.to_datetime(df["Data"])
df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]

# CREA CATEGORIA
mappa = {
    "Smartphone": "Informatica",
    "Laptop": "Informatica", 
    "Tablet": "Informatica",
    "TV": "Elettrodomestici",
    "Cuffie": "Accessori"
}
df["Categoria"] = df["Prodotto"].map(mappa)

# ANALISI PER CATEGORIA
per_cat = df.groupby("Categoria").agg({
    "Incasso": "sum",
    "Quantità": "mean"
}).round(2)
per_cat.columns = ["Incasso_totale", "Quantità_media"]

print("Analisi per categoria:")
print(per_cat)

# SALVA
df.to_csv("vendite_analizzate.csv", index=False)
print(f"\n✓ Salvato vendite_analizzate.csv ({len(df)} righe, {len(df.columns)} colonne)")
