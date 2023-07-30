import time

def busqueda_lineal(lista, elemento_buscado):
    elemento_encontrado = None
    for elemento in lista:
        if elemento == elemento_buscado:
            elemento_encontrado = elemento
            return elemento_encontrado
    return None

inicio = time.time()
# Código a medir
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
encontrado = busqueda_lineal(lista, 20)
print(encontrado)
# -------------
fin = time.time()
total = fin - inicio
print("%.6f" % total) # Tiempo que tardo en ejecutarse