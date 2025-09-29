import pandas as pd
import csv

datos = pd.read_csv("datos_canciones.csv")
#print(datos)


#with open("datos_canciones.csv",newline='',encoding='utf-8') as f:
#    reader = csv.reader(f)
#    for fila in reader:
#        print(fila)

print(datos.head()) #Primeras cinco filas
print(datos.shape) #Tamaño del dataset
print(datos.columns) #Revisar el nombre de las columnas
print(datos['view_count'].value_counts())
print(datos['duration'].value_counts())
print(datos['categories'].value_counts())
print(datos['tags'].value_counts())






