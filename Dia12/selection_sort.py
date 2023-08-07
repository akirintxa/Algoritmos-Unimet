def selection_sort(lista):
  tamanio = len(lista)
  for i in range(tamanio - 1):
    print("Revision ", i + 1)
    print(lista)
    posicion_minimo = i
    print("Minimo actual: ", lista[i])
    # Buscamos el menor en la parte derecha desordenada
    for j in range(i + 1, tamanio):
      # Si hay un elemento menor al actual, guardamos su posicion
      if lista[j] < lista[posicion_minimo]:
        posicion_minimo = j
        print("Nuevo minimo: ", lista[j])
    # Intercambiamos los elementos
    lista[i], lista[posicion_minimo] = lista[posicion_minimo], lista[i]
    print(lista, "\n")

  return lista


lista = [8, 4, 2, 6, 9]
lista = selection_sort(lista)
print(lista)