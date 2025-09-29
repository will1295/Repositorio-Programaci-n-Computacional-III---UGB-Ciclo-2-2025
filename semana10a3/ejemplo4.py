import pandas as pd

datos = pd.read_csv("datos_bmw.csv")
print(datos.columns)

print(f"Media:  ${datos['Price_USD'].mean()}")
print(f"Valor de venta mas bajo:  ${datos['Price_USD'].min()} ")
print(f"Valor de venta mas alto:  ${datos['Price_USD'].max()} ")
print(f"Variacion de precios:  ${datos['Price_USD'].var()} ")
print(f"Dispersion de precios:  ${datos['Price_USD'].std()} ")
precios = datos['Price_USD']
print(precios.quantile([0.25,0.5,0.75]))

print(f"Media de Kilometraje:  {datos['Mileage_KM'].mean()}")
print(f"Kilometraje mas bajo:  {datos['Mileage_KM'].min()} ")
print(f"Kilometraje mas alto:  {datos['Mileage_KM'].max()} ")

print(f"Color más popular de carro:  {datos['Color'].mode()[0]}")

