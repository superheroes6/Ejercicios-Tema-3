def recursivo(matriz):
    if len(matriz) == 2:
        return matriz[0][0] * matriz[1][1] - matriz[0][1] * matriz[1][0]
    else:
        det = 0
        for i in range(len(matriz)):
            submatriz = []
            for fila in matriz[1:]:
                nueva_f = fila[:i] + fila[i+1:]
                submatriz.append(nueva_f)
        
            det += ((-1) ** i) * matriz[0][i] * recursivo(submatriz)
        return det

matriz = [
    [4, 3, 2],
    [3, 2, 1],
    [2, 1, 0]
]

determinante = recursivo(matriz)
print(f"El determinante es: {determinante}")