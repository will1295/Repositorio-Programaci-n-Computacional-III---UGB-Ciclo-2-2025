import pandas as pd

datos = pd.read_csv("datos_vuelos.csv")
print(datos.head())
print(datos.shape)
print(datos.columns)
print(datos.info())

print(datos['dest'].value_counts())
print(datos['origin'].value_counts())

print(f"Dia de la semana más frecuente: {datos['day_of_week'].mode()[0]}")
print(f"Mes más frecuente: {datos['month'].mode()[0]}")
print(f"Dia del mes más frecuente: {datos['day_of_month'].mode()[0]}")
