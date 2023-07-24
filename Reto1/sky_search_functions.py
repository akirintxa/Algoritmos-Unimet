import sky_show_functions as skyshow
import check


def search_data_menu(data):
    """Muestra un menú interactivo para buscar datos meteorológicos.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra el menú.
    """
    while True:
        option = input("""
=== MENU 3: BUSCAR DATOS METEREOLÓGICOS ===
Seleccione una opción:
    1. Buscar por fecha
    2. Buscar por tipo de variable climática
    3. Buscar por tipo y valor de variable climática
    0. Regresar o salir
             
""")
        if option == "1":
            country_option = input("Escriba el país a consultar: ")
            locations = skyshow.get_all_locations(data)
            if check.is_in_list(locations, country_option):
                date_option = input(
                    "Introduzca la fecha en formato AAAA/MM/DD: ")
                date_search(data, country_option, date_option)
            else:
                print(f"""
*** Ese país no está en la lista
Los países disponibles son:
{locations}""")

        elif option == "2":
            country_option = input("Escriba el país a consultar: ")
            locations = skyshow.get_all_locations(data)
            if check.is_in_list(locations, country_option):
                print(f"""
Estas son las variables disponibles para consultar:
    1. Temperatura
    2. Humedad
    3. Velocidad del viento""")
                while True:
                    option = input(
                        "Introduzca el número de la variable a consultar (1, 2 o 3): ")
                    if option in ["1", "2", "3"]:
                        option = int(option)
                        variable_search(data, country_option, option)
                        break
                    else:
                        print(
                            "\n*** Por favor elija sólo una de las opciones disponibles.")
            else:
                print(f"""
*** Ese país no está en la lista
Los países disponibles son:
{locations}""")

        elif option == "3":
            variable_value_search(data)

        elif option == "0" or option.lower() == "salir":
            break

        else:
            print("*** Por favor elija sólo una de las opciones disponibles.")


def date_search(data, country_name, date):
    """Busca datos meteorológicos para una ubicación específica y una fecha dada.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.
        country_name (str): El nombre del país para el cual se desean buscar los datos.
        date (str): La fecha en formato AAAA/MM/DD que se desea buscar.

    Returns:
        None: La función no devuelve ningún valor, solo imprime los datos encontrados o mensajes de error.
    """
    found = False
    count = 0

    for country_data in data:  # Recorro la lista externa y me devuelve diccionario
        # Comparo si el location_name es el pais que quiero
        if country_data["location_name"].lower() == country_name.lower():
            # Recorro la lista de location_measurements
            for measurement in country_data["location_measurements"]:
                if measurement["date"] == date:  # Si el key de fecha coincide con la quiero
                    print(f"""
Fecha: {measurement['date']}
Temperatura: {measurement['temperature']}
Humedad: {measurement['humidity']}
Velocidad del viento: {measurement['wind_speed']}
""")
                    found = True
                    count += 1
            print(
                f"\n--> Se encontraron {count} mediciones para la fecha '{date}' de {country_name.upper()}.")
            break

    if not found:
        print("\n*** Revise el formato de la fecha.")


def translate_option(option):
    """Traduce una opción numérica a su correspondiente variable en inglés.

    Parameters:
        option (int): La opción numérica que se desea traducir.

    Returns:
        str or None: La variable en inglés correspondiente a la opción, o None si la opción no es válida o no está disponible.
    """
    # Diccionario con la traducción de opciones numéricas a variables en inglés
    option_dict = {
        1: "temperature",
        2: "humidity",
        3: "wind_speed",
    }
    return option_dict.get(option)


def variable_search(data, country_name, option):
    """Busca datos meteorológicos para una ubicación específica y una opción dada.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.
        country_name (str): El nombre del país para el cual se desean buscar los datos.
        option (int): La opción numérica que se desea buscar (1 para temperatura, 2 para humedad, 3 para velocidad del viento).

    Returns:
        None: La función no devuelve ningún valor, solo imprime los datos encontrados o mensajes de error.
    """
    found = False
    count = 0

    translated_variable = translate_option(option)
    if translated_variable is None:
        print("\n*** Opción no válida o no disponible en los datos.")
        return

    for country_data in data:
        if country_data["location_name"].lower() == country_name.lower():
            for measurement in country_data["location_measurements"]:
                if translated_variable in measurement:
                    print(f"""
Fecha: {measurement['date']}
{translated_variable.title()}: {measurement[translated_variable]}
""")
                    found = True
                    count += 1

            print(
                f"\nSe encontraron {count} mediciones.")
            break

    if not found:
        print("\n*** No hay datos para esa opción o el nombre del país no es correcto.")


def variable_value_search(data):
    """Busca y muestra los datos meteorológicos de un país para una variable y valor específico.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.

    Returns:
        None: La función no devuelve ningún valor, solo imprime los datos encontrados o mensajes de error.
    """
    country_option = input("Escriba el país a consultar: ")
    locations = skyshow.get_all_locations(data)
    count = 0

    if not check.is_in_list(locations, country_option):
        print(f"\n*** El país '{country_option}' no está en la lista.")
        return

    print(f"""
Estas son las variables disponibles para consultar:
    1- Temperatura
    2- Humedad
    3- Velocidad del viento""")

    while True:
        option = input(
            "Introduzca el número de la opción a consultar (1, 2 o 3): ")
        if option in ["1", "2", "3"]:
            option = int(option)
            break
        else:
            print("\n*** Opción no válida. Intente nuevamente.")

    variable_options = {
        1: "temperature",
        2: "humidity",
        3: "wind_speed"
    }
    variable_option = variable_options.get(option)

    value = input(f"Introduzca el valor a buscar: ")

    found = False
    for country_data in data:
        if country_data["location_name"].lower() == country_option.lower():
            for measurement in country_data["location_measurements"]:
                if variable_option in measurement:
                    try:
                        if float(measurement[variable_option]) == float(value):
                            print(f"""
Fecha: {measurement['date']}
{variable_option.title()}: {measurement[variable_option]}
""")
                            found = True
                            count += 1
                    except ValueError:
                        pass
            print(f"\nSe encontraron {count} mediciones.")

            if not found:
                print("\n*** No hay datos que coincidan con el valor especificado.")
            break
