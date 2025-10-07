import pandas as pd

datos = pd.read_csv("datos_ventas.csv")
print(datos)

#Primeros cinco valores o la cantidad que se especifique
print(datos.head())

#Ultimos cinco valores o la cantidad que se especifique
print(datos.tail())

print(datos.columns)

print(datos['Year'])
rango = datos[(datos['Year'] >=2020) & (datos['Year']<= 2021)]
print(rango)

print(f"Media: {datos['Price_USD'].mean()}")
print(f"Mediana: {datos['Price_USD'].median()}")
print(f"Varianza: {datos['Price_USD'].var()}")
print(f"Desviacion estandar: {datos['Price_USD'].std()}")
print(f"Precio mas bajo: {datos['Price_USD'].min()}")
print(f"Precio mas alto: {datos['Price_USD'].max()}")

print(f"Color mas popular: {datos['Color'].mode()[0]}")

print(f"Media: {datos['Mileage_KM'].mean()}")
print(f"Kilometraje mas alto: {datos['Mileage_KM'].max()}")

kmalto = datos[datos['Mileage_KM']>10000].tail()
print(f"Carros que superan los 100,000 km: {kmalto}")
