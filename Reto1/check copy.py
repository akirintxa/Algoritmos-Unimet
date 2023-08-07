def is_number(value):
    try:
        # print("Es válido")
        int(value)
        return True

    except Exception as e:
        # print(e)
        # print("No es válido")
        return False


def is_in_range(number, start, end):
    if number >= start and number <= end:
        return True
    else:
        return False


def is_in_list(list_name, element):
    """Verifica si un elemento está presente en una lista, ignorando diferencias de mayúsculas y minúsculas.

    Parameters:
        list_name (list): La lista en la que se buscará el elemento.
        element: El elemento que se desea buscar en la lista.

    Returns:
        bool: True si el elemento está presente en la lista, False en caso contrario.
    """
    for item in list_name:
        if item.lower() == element.lower():
            return True
    return False
