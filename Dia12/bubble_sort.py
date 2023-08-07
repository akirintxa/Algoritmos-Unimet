def bubble_sort(lista):
    tamanio = len(lista)
    # Desde 1 hasta tamaño - 1. Representa cada revision de la lista por completo.
    for i in range(1, tamanio):
        # Desde 0 hasta tamaño - i. Los menores
        print("\nRevision ", i, "\n") 
        for j in range(0, tamanio - i):
            print("Lista a revisar: ")
            lista_a_revisar = lista[0 : tamanio - i + 1]
            print(lista_a_revisar, "\n")
            # lista[j] = Elemento izquierdo
            # lista[j + 1] = Elemento derecho
            # Si elemento izquierdo es mayor que elemento derecho...
            print("Elemento izquierdo: ", lista[j])
            print("Elemento derecho: ", lista[j + 1])
            if lista[j] > lista[j + 1]:
                # Intercambiamos los elementos
                lista[j], lista[j + 1] = lista[j + 1], lista[j]
            print("Lista resultante:")
            print(lista, "\n")
    return lista

lista = [8, 4, 2, 6, 9]
lista = bubble_sort(lista)
print(lista)

lista2 = ['f','e','d','c','b','a']

lista = bubble_sort(lista2)
print(lista2)