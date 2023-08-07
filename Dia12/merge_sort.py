def merge_sort(lista):
  # Si la lista tiene 1 o ningun elemento, se retorna
  if (len(lista) <= 1):
    return lista
  # Posicion en la mitad de la lista
  posicion_medio = len(lista) // 2
  # Ordenamos y fusionamos cada mitad
  lista_izquierda = merge_sort(lista[ : posicion_medio])
  lista_derecha = merge_sort(lista[posicion_medio : ])
  # Fusionamos las listas ordenadas en un nueva ordenada
  return merge(lista_izquierda, lista_derecha)

def merge(lista_izquierda, lista_derecha):
    # Creamos una lista vacia
    lista_ordenada = []
    # Inicializamos en el primer elemento de cada lista
    posicion_izquierda = 0
    posicion_derecha = 0
    # Guardamos el tamaño de cada lista
    if(lista_izquierda == None):
        lista_izquierda = []
    if(lista_derecha == None):
        lista_derecha = []
    tamanio_izquierda = len(lista_izquierda)
    tamanio_derecha = len(lista_derecha)
    for i in range(tamanio_izquierda + tamanio_derecha):
        if(posicion_izquierda < tamanio_izquierda and posicion_derecha < tamanio_derecha):
            # Comprobamos el menor de ambas listas, si es el de la izquierda se añade a la lista ordenada
            if (lista_izquierda[posicion_izquierda] <= lista_derecha[posicion_derecha]):
                lista_ordenada.append(lista_izquierda[posicion_izquierda])
                # Aumentamos la posicion izquierda
                posicion_izquierda += 1
            # Si el menor es el de la derecha, se añade a la lista ordenada
            else:
                lista_ordenada.append(lista_derecha[posicion_derecha])
                # Aumentamos la posicion derecha
                posicion_derecha += 1
        # Si llegamos al final de la lista izquierda, entonces agregamos los elementos de la lista derecha
        elif(posicion_izquierda == tamanio_izquierda):
            lista_ordenada.append(lista_derecha[posicion_derecha])
            # Aumentamos la posicion derecha
            posicion_derecha += 1
        # Si llegamos al final de la lista derecha, entonces agregamos los elementos de la lista izquierda
        elif(posicion_derecha == tamanio_derecha):
            lista_ordenada.append(lista_izquierda[posicion_izquierda])
            # Aumentamos la posicion izquierda
            posicion_izquierda += 1
    return lista_ordenada


lista = [8, 4, 2, 6, 9]
lista = merge_sort(lista)
print(lista)