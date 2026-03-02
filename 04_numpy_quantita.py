import pandas as pd
import numpy as np

df = pd.read_csv("vendite.csv")
df["Data"] = pd.to_datetime(df["Data"])
df["Incasso"] = df["Quantità"] * df["Prezzo_unitario"]

# ESTRAI ARRAY NUMPY
q = df["Quantità"].to_numpy()
print("Array Quantità:", q[:10], "...")

# CALCOLI RICHIESTI
media = np.mean(q)
minimo = np.min(q)
massimo = np.max(q)
dev_std = np.std(q)  # popolazione (default)

print(f"\nMedia: {media:.2f}")
print(f"Minimo: {minimo}")
print(f"Massimo: {massimo}")
print(f"Deviazione standard: {dev_std:.2f}")

# PERCENTUALE SOPRA MEDIA
sopra_media = (q > media).mean() * 100
print(f"Percentuale vendite sopra media: {sopra_media:.1f}%")

# VERIFICA INCASSO CON NUMPY 2D
arr2d = df[["Quantità", "Prezzo_unitario"]].to_numpy()
incassi_np = arr2d[:, 0] * arr2d[:, 1]
print(f"\nVerifica NumPy vs Pandas: {np.allclose(incassi_np, df['Incasso'].to_numpy())}")
