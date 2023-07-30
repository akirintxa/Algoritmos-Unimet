def vaciar_lista_iterativo(lista):
    inicio = len(lista) - 1  # Inicia en tamanio - 1
    fin = -1  # No se incluye asi que llega hasta 0
    step = -1  # Va de 1 en 1 decreciendo
    for i in range(inicio, fin, step):
        print("Posicion donde se eliminara: ", i)
        print("Listas ANTES: ", lista)
        lista.pop(i)
        print("Listas DESPUES: ", lista, "\n")


def vaciar_lista_recursivo(lista, llamada):
    print("\nllamada numero: ", llamada)
    print("Lista que recibe la llamada: ", lista)
    # Mientras la lista este llena, eliminamos
    if (len(lista) != 0):
        # Eliminamos el elemento final
        lista.pop()
        # Llamamos de nuevo la funcion
        print(
            f"Llamamos a la funcion de nuevo. PAUSA de la llamada: {llamada}.")
        siguiente_llamada = llamada + 1
        vaciar_lista_recursivo(lista, siguiente_llamada)  # PAUSA por llamada
        print(f"PLAY de la llamada: {llamada}.")
    # Una vez la lista esta vacia, se lo indicamos al usuario
    else:
        print("\nPUNTO DE QUIEBRE ENCONTRADO")
        print("La lista esta vacia.")
    print(f"FINALIZA la llamada: {llamada}.\n")


lista = [1, 2, 3, 4]
llamada = 1
print("ANTES")
print(lista)
print()

# Iterativo
# vaciar_lista_iterativo(lista)
# Recursivo
vaciar_lista_recursivo(lista, llamada)

print()
print("DESPUES")
print(lista)
