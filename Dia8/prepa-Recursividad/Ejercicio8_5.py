def reverse_list(lista_original):
    if len(lista_original) > 0:
        element = lista_original.pop()
        lista_original = reverse_list(lista_original)
        lista_original.insert(0, element)
        return lista_original
    else:
        return []


def start():
    lista = [1,2,3,4,5,6,7,8,9,10]
    
    print(lista)
    print(reverse_list(lista))


start()