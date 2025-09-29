import numpy as np

edades = np.array([20,19,19,21,18,22,25,18,18,19,20])

print("Media aritmetica: ", np.mean(edades))
print("Mediana: ", np.median(edades))
print("Varianza: ", np.var(edades))
print("Desviacion estandar: ", np.std(edades))
print("Valor minimo: ", np.min(edades))
print("Valor maximo: ", np.max(edades))