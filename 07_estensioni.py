import pandas as pd
import matplotlib.pyplot as plt

def top_n_prodotti(df, n=3):
    """Restituisce n prodotti più venduti per INCASSO"""
    return (df.groupby("Prodotto", as_index=False)["Incasso"]
            .sum()
            .sort_values("Incasso", ascending=False)
            .head(n))

# Carica
df = pd.read_csv("vendite.csv")
df["Data"] = pd.to_datetime(df["Data"])
df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]
df["Categoria"] = df["Prodotto"].map({
    "Smartphone": "Informatica", "Laptop": "Informatica", 
    "Tablet": "Informatica", "TV": "Elettrodomestici", "Cuffie": "Accessori"
})

# FUNZIONE TOP N
print("Top 3 per incasso:")
print(top_n_prodotti(df, 3))

# GRAFICO COMBINATO
per_cat = df.groupby("Categoria").agg({
    "Incasso": "mean", "Quantità": "mean"
}).round(2)

fig, ax1 = plt.subplots(figsize=(9, 5))

# Barre incasso medio
per_cat["Incasso"].plot(kind="bar", ax=ax1, color="steelblue", alpha=0.7)
ax1.set_ylabel("Incasso medio (€)", color="steelblue")
ax1.tick_params(axis='y', labelcolor="steelblue")

# Linea quantità media
ax2 = ax1.twinx()
per_cat["Quantità"].plot(ax=ax2, color="darkorange", linewidth=3, marker="o")
ax2.set_ylabel("Quantità media", color="darkorange")
ax2.tick_params(axis='y', labelcolor="darkorange")

plt.title("Incasso medio + Quantità media per categoria")
fig.tight_layout()
plt.show()

print("✓ Estensioni completate")
