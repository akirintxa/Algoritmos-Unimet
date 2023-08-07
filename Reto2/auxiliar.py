import skynow_show as show


def country_exists(countries_data, country_name):
    """Verifica si el país buscado existe en la lista de objetos Country.

    Parameters:
        countries_data (list): Una lista de objetos Country que contiene información de los países.
        country_name (str): El nombre del país buscado.

    Returns:
        bool: True si el país existe en la lista, False si no existe.
    """
    for country in countries_data:
        if country.name.lower() == country_name.lower():
            return True

    return False


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


def is_valid_date(date_str):
    """Check if a date string is in the format 'AAAA/MM/DD'.

    Parameters:
        date_str (str): The date string to be checked.

    Returns:
        bool: True if the date string is in the format 'AAAA/MM/DD', False otherwise.
    """
    try:
        year, month, day = map(int, date_str.split('/'))
        if len(date_str) == 10 and date_str[4] == date_str[7] == '/' and 1 <= month <= 12 and 1 <= day <= 31:
            return True
        else:
            return False
    except ValueError:
        return False


def binary_search(states_list, state_name):
    inicio = 0
    fin = len(states_list) - 1
    while inicio <= fin:
        medio = (inicio + fin) // 2  # División entera para conseguir la mitad
        if states_list[medio].name.lower() == state_name.lower():
            # Si el estado medio es el buscado
            return states_list[medio]
        elif states_list[medio].name.lower() < state_name.lower():
            # Si el estado buscado es mayor al estado medio
            inicio = medio + 1
        else:
            # Si el estado buscado es menor al estado medio
            fin = medio - 1
    return None  # Devolver None en caso de no encontrar el estado
