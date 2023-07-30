import time

def busqueda_binaria(lista, elemento_buscado): 
    inicio = 0
    fin = len(lista) - 1
    while inicio <= fin:
        print("INICIO: ", inicio)
        print("FIN: ", fin)
        medio = (inicio + fin) // 2 # Division entera para conseguir la mitad
        print("MEDIO: ", medio)
        if lista[medio] == elemento_buscado:
            # Si el elemento medio es el buscado
            print("ENCONTRADO")
            return lista[medio]
        elif lista[medio] < elemento_buscado:
            # Si el elemento buscado es mayor que el medio
            print("Busquemos en la mitad mayor (derecha)")
            inicio = medio + 1
        else:
            # Si el elemento buscado es menor que el medio
            print("Busquemos en la mitad menor (izquierda)")
            fin = medio - 1
    print("NO ENCONTRADO")
    return None

def busqueda_binaria_recursiva(lista, elemento_buscado, inicio, fin):
    print(lista[inicio:fin + 1])
    if inicio > fin:
        return None
    medio = (inicio + fin) // 2 # Division entera para conseguir la mitad
    if lista[medio] == elemento_buscado:
        # Si el elemento medio es el buscado
        print("ENCONTRADO")
        return lista[medio]
    elif lista[medio] < elemento_buscado:
        # Si el elemento buscado es mayor que el medio
        print("Busquemos en la mitad mayor (derecha)")
        return busqueda_binaria_recursiva(lista, elemento_buscado, medio + 1, fin)
    else:
        # Si el elemento buscado es menor que el medio
        print("Busquemos en la mitad menor (izquierda)")
        return busqueda_binaria_recursiva(lista, elemento_buscado, inicio, medio - 1)



inicio = time.time()
# Código a medir
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
encontrado = busqueda_binaria(lista, 0)
#inicio_busqueda = 0
#fin_busqueda = len(lista) - 1
#encontrado = busqueda_binaria_recursiva(lista, 10, inicio_busqueda, fin_busqueda)
print(encontrado)
# -------------
fin = time.time()
total = fin - inicio
print("%.6f" % total) # Tiempo que tardo en ejecutarse