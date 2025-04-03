def mover(n, origen, destino, auxiliar):
    if n == 1:
        print(f"mueve la piedra de {origen} a {destino}")
        return
    mover(n - 1, origen, auxiliar, destino)
    print(f"mueve la piedra de {origen} a {destino}")
    mover(n - 1, auxiliar, destino, origen)

mover(74, "Columna A", "Columna B", "Columna C")