import numpy as np

def restar(po1, po2):
    resta = np.polysub(po1, po2)
    return resta

def dividir(po1, po2):
    division = np.polydiv(po1, po2)
    return division

def eliminar(polinomio, termino):
    polinomio = list(polinomio)
    if termino in polinomio:
        polinomio.remove(termino)
    return polinomio

def existe(polinomio, termino):
    exist = termino in polinomio
    return exist

p1 = [3, 2, 1]
p2 = [1, 0, -1]

print("Resta de polinomios:", restar(p1, p2))

cociente, residuo = dividir(p1, p2)
print("Division de polinomios: Cociente:", cociente, "Residuo:", residuo)

termino_a_eliminar = 2
print("Polinomio despues de eliminar el termino", termino_a_eliminar, ":", eliminar(p1, termino_a_eliminar))

termino_a_buscar = 3
print("Existe el termino", termino_a_buscar, "en el polinomio?", existe(p1, termino_a_buscar))