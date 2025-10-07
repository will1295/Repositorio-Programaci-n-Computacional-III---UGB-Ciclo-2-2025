import pandas as pd

datos = pd.read_csv("datos_vuelos.csv")

print(datos.columns)

print(f"Promedio de tiempo de despegue: {datos['dep_delay'].mean()}")

print(f"Promedio de tiempo de aterrizaje: {datos['arr_delay'].mean()}")

print(f"Mes mas frecuente de vuelos: {datos['month'].mode()[0]}")

print(f"Mes mas frecuente de vuelos: {datos['month'].mode()[0]}")

print(f"Destino mas frecuente de vuelos: {datos['dest_city_name'].mode()[0]}")

print(f"Estado mas frecuente de vuelos: {datos['dest_state_nm'].mode()[0]}")