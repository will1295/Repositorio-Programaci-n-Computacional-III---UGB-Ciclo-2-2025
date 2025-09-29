import numpy as np

#vector unidimensional
vector = np.array([1,2,3,4])
print(vector)
print(vector.shape)

print(vector[1])

matriz = np.array([[1,2,3,4],[5,6,7,8]])
print(matriz)
print(matriz.shape)
print(matriz[1,1])

matriz3d = np.array([
    [[1,2,3],
     [4,5,6],
     [7,8,9]],
     [[10,11,12],
      [13,14,15],
      [16,17,18]]
])

print(matriz3d)
print(matriz3d.shape)
print(matriz3d[1,1,0])
