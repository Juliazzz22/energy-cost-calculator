import pandas as pd

# CSV-Datei einlesen
df = pd.read_csv("example_data.csv")

# CO2-Faktor für Gas
co2_factor_gas = 0.2  # t/MWh

# Kosten berechnen
df["electricity_cost"] = df["electricity_consumption_mwh"] * df["electricity_price_eur_per_mwh"]
df["gas_cost"] = df["gas_consumption_mwh"] * df["gas_price_eur_per_mwh"]
df["co2_cost"] = df["gas_consumption_mwh"] * co2_factor_gas * df["co2_price_eur_per_ton"]

# Gesamtkosten
df["total_cost"] = df["electricity_cost"] + df["gas_cost"] + df["co2_cost"]

print(df)
print()
print("Total system cost:", df["total_cost"].sum(), "€")
