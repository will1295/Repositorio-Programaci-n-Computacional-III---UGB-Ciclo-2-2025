import numpy as np

edades = [20,19,18,19,19,17,17,16,28,20,21,19,18,20,21,21,17]

print(f"Media aritmetica : {np.mean(edades)}")
print(f"Mediana : {np.median(edades)}")
print(f"Varianza : {np.var(edades)}")
print(f"Desviacion estandar : {np.std(edades)}")
print(f"Edad minima : {np.min(edades)}")
print(f"Edad maxima : {np.max(edades)}")

