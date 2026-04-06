gas_price = 40           # €/MWh
co2_price = 100          # €/t

# Example consumption
electricity_consumption = 150  # MWh
gas_consumption = 200          # MWh

# CO2 factors
co2_factor_gas = 0.2  # t/MWh

# Cost calculation
electricity_cost = electricity_consumption * electricity_price
gas_cost = gas_consumption * gas_price
co2_cost = gas_consumption * co2_factor_gas * co2_price

total_cost = electricity_cost + gas_cost + co2_cost

print("Electricity cost:", electricity_cost, "€")
print("Gas cost:", gas_cost, "€")
print("CO2 cost:", co2_cost, "€")
print("Total cost:", total_cost, "€")
