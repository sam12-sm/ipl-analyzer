import pandas as pd

matches = pd.read_csv("data/matches.csv")
deliveries = pd.read_csv("data/deliveries.csv")

print("=== MATCHES DATASET ===")
print(f"Rows: {matches.shape[0]}, Columns: {matches.shape[1]}")
print("\nColumn Names:")
print(matches.columns.tolist())
print("\nFirst 3 rows:")
print(matches.head(3))


print("=== DELIVERIES DATASET ===")
print(f"Rows: {deliveries.shape[0]}, Columns: {deliveries.shape[1]}")
print("\nColumn Names:")
print(deliveries.columns.tolist())