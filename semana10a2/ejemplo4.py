import pandas as pd

datos = pd.read_csv("datos_ventas.csv")
print(datos.columns)

print(f"Precio de venta mas alto: {datos.max()}")
print(f"Precio de venta mas bajo: {datos.min()}")

print(f"Promedio de precio de venta: ${datos['Price_USD'].mean()}")
print(f"Color mas popular de carro: {datos['Color'].mode()[0]}")
print(datos['Color'].value_counts())
print(f"Variacion entre colores: {datos['Color'].value_counts().std()}")

print(f"Promedio del kilometraje: {datos['Mileage_KM'].mean()}")

precios = datos['Price_USD']

print(precios.quantile([0.25,0.5,0.75]))

rango = datos[(datos['Price_USD'] >= 40000) & datos['Price_USD'] <= 80000]
print(rango)

