import numpy as np

def iterativo(matriz):
    return np.linalg.det(matriz)

matriz = [
    [4, 3, 2],
    [3, 2, 1],
    [2, 1, 0]
]

determinante = iterativo(matriz)
print(f"El determinante es: {determinante}")