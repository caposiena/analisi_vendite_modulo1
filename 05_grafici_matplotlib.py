import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("vendite.csv")
df["Data"] = pd.to_datetime(df["Data"])
df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]

# 1. BARRE: incasso totale per negozio
plt.figure(figsize=(8, 5))
df.groupby("Negozio")["Incasso"].sum().sort_values(ascending=False).plot(kind="bar", color="steelblue")
plt.title("Incasso totale per negozio")
plt.ylabel("Euro")
plt.xlabel("Negozio")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# 2. TORTA: % incassi per prodotto
plt.figure(figsize=(8, 8))
df.groupby("Prodotto")["Incasso"].sum().plot(kind="pie", autopct="%1.1f%%")
plt.title("Percentuale incassi per prodotto")
plt.ylabel("")
plt.tight_layout()
plt.show()

# 3. LINEE: andamento giornaliero
daily_incasso = df.groupby(df["Data"].dt.date)["Incasso"].sum().sort_index()
plt.figure(figsize=(10, 5))
daily_incasso.plot(kind="line", marker="o", linewidth=2, markersize=8)
plt.title("Andamento giornaliero incassi totali")
plt.ylabel("Euro")
plt.xlabel("Data")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

print("✓ 3 grafici generati")
