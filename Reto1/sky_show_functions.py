import check


def show_data_menu(data):
    """Muestra un menú interactivo para ver datos meteorológicos.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra el menú.
    """
    while True:
        option = input("""
=== MENU 1: VER DATOS METEOROLÓGICOS ===
Seleccione una opción:
    1. Mostrar ubicaciones
    2. Mostrar información de una ubicación
    0. Regresar o salir
                       
""")
        if option == "1":
            print(f"\nLas ubicaciones disponibles para consultar son: ")
            locations = get_all_locations(data)
            print(locations)

        elif option == "2":
            country_option = input("Escriba el país a consultar: ")
            locations = get_all_locations(data)
            if check.is_in_list(locations, country_option):
                measurements = get_weather_data_of_country(
                    data, country_option)
                for measurement in measurements:
                    print(f"""
Fecha: {measurement['date']}
Temperatura: {measurement['temperature']}
Humedad: {measurement['humidity']}
Velocidad del viento: {measurement['wind_speed']}
""")
                print(f"""
--> Se encontraron {len(measurements)} mediciones disponibles para {country_option.upper()}
""")
            else:
                print(f"""
*** Ese país no está en la lista
Los países disponibles son:
{locations}""")

        elif option == "0" or option.lower() == "salir":
            break

        else:
            print("*** Por favor elija sólo una de las opciones disponibles.")


def get_all_locations(data):
    """Obtiene una lista de todas las ubicaciones disponibles en los datos meteorológicos.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.

    Returns:
        list: Una lista que contiene los nombres de todas las ubicaciones disponibles.
    """
    countries = []
    for location in data:
        country = location["location_name"]
        countries.append(country)
    return countries


def get_weather_data_of_country(data, country_name):
    """Obtiene todos los datos meteorológicos de un país específico.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.
        country_name (str): El nombre del país para el cual se desean obtener los datos.

    Returns:
        list: Una lista que contiene los datos meteorológicos disponibles para el país especificado.
    """
    country_measurements = []
    for country_data in data:
        if country_data["location_name"].lower() == country_name.lower():
            for measurement in country_data["location_measurements"]:
                country_measurements.append(measurement)
    return country_measurements


def get_weather_variables(data):
    """Obtiene una lista de las variables climáticas disponibles en los datos meteorológicos.

    Recorre la lista de datos meteorológicos y recopila todas las claves (variables climáticas)
    presentes en las mediciones. Utiliza un conjunto para evitar duplicados y luego convierte
    el conjunto en una lista.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.

    Returns:
        list: Una lista que contiene las variables climáticas disponibles.
    """
    variables = set()  # No me funcionó crearlo como variables = {}
    for location in data:
        for measurement in location["location_measurements"]:
            variables.update(measurement.keys())
    if "date" in variables:
        variables.remove("date")

    return list(variables)
