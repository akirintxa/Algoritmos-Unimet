def insertion_sort(lista):
    tamanio = len(lista)
    for i in range(1, tamanio):
        print("Revision ", i)
        print(lista)
        elemento = lista[i]
        print("Elemento actual: ", elemento)
        j = i - 1
        # Mientras los elementos de la izquierda sean mayores a elemento
        while j >= 0 and lista[j] > elemento:
            print("Elemento izquierdo: ", lista[j])
            # Se mueven los mayores a la derecha
            lista[j + 1] = lista[j]
            # Le restamos una posicion a j para ir a la izquierda
            j -= 1
            print("Burbujea a la derecha: ", lista)
        # Agregamos el elemento en la posicion correcta
        lista[j + 1] = elemento
        print(lista, "\n")

    return lista

lista = [8, 4, 2, 6, 9]
lista = insertion_sort(lista)
print(lista)