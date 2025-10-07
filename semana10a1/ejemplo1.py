import numpy as np

arreglo1 = np.array([1,2,3,4,5,6])
print(arreglo1)
print(arreglo1.shape)

print(arreglo1[2])

matriz1 = np.array([[1,2,3,4,5,6],
                   [7,8,9,10,11,12]])
print(matriz1)
print(matriz1.shape)

print(matriz1[1][2])

matriz2 = np.array([[[1,2,3,4,5,6],
                    [7,8,9,10,11,12],
                    [13,14,15,16,17,18]],
                    [[4,1,2,4,55,1],
                    [4,12,43,11,21,5],
                    [1,4,47,9,11,21]]])

print(matriz2)
print(matriz2.shape)
print(matriz2.max())
print(matriz2[1][1][2])
