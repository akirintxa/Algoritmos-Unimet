def report_menu(countries_data, states_data, measurements_data):
    while True:
        option = input("""
    === MENU 1: GENERAR REPORTES ===
    Seleccione una opción:
        1. Mostrar países
        2. Mostrar información de un país
        3. Mostrar estados de un país
        4. Mostrar datos meteorológicos de un país
        0. Regresar o salir
                       
""")
        if option == "1":
            show_country_list(countries_data)

        elif option == "2":
            show_country_list(countries_data)
            country_option = input("Escriba el país a consultar: ")
            show_country_info(countries_data, country_option)

        elif option == "3":
            show_country_list(countries_data)
            country_option = input("Escriba el país a consultar: ")
            show_all_states(states_data, country_option)

        elif option == "4":
            show_country_list(countries_data)
            country_option = input("Escriba el país a consultar: ")
            show_country_weather(measurements_data, country_option)

        elif option == "0" or option.lower() == "salir":
            break

        else:
            print("*** Por favor elija sólo una de las opciones disponibles.")


def show_country_list(countries_data):
    countries = get_all_countries(countries_data)
    print("Los países disponibles son:", ", ".join(countries))


def get_all_countries(countries):
    """Obtiene una lista de todos los países disponibles.

    Parameters:
        countries (list): Una lista de objetos Country que contiene información de los países.

    Returns:
        list: Una lista que contiene los nombres de todos los países disponibles.
    """
    country_names = []
    for country in countries:
        country_names.append(country.name)
    return country_names


def show_country_info(countries_data, country_name):
    """Muestra la información de un país específico.

    Parameters:
        countries_data (list): Una lista de objetos Country que contiene información de los países.
        country_name (str): El nombre del país a consultar.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra la información del país.
    """
    found_country = None
    for country in countries_data:
        if country.name.lower() == country_name.lower():
            found_country = country
            break

    if found_country:
        print("\nInformación del país:")
        found_country.print_country_info()  # Usamos el método de la clase country
    else:
        print(
            f"""
El país '{country_name.upper()}' no fue encontrado en la lista de países.
""")


def show_all_states(states_data, country_name):
    """Muestra los estados de un país específico.

    Parameters:
        states_data (list): Una lista de objetos State que contiene información de los estados.
        country_name (str): El nombre del país cuyos estados se desean mostrar.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra los estados del país.
    """
    found_states = []

    for state in states_data:  # Iteramos sobre cada objeto State en states_data.
        if state.country.lower() == country_name.lower():
            found_states.append(state)

    if found_states:
        print(f"\nEstados de {country_name.upper()}:\n")
        for state in found_states:
            print(state.name)
    else:
        print(
            f"\nEl país '{country_name.upper()}' no tiene estados registrados.")


def show_country_weather(measurements_data, country_name):
    """Muestra los datos meteorológicos de un país específico.

    Parameters:
        measurements_data (list): Una lista de objetos Measurement que contiene información meteorológica.
        country_name (str): El nombre del país cuyos datos meteorológicos se desean mostrar.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra los datos meteorológicos.
    """
    found_measurements = []

    # Iteramos sobre cada objeto Measurement en measurements_data.
    for measurement in measurements_data:
        if measurement.location_name.lower() == country_name.lower():
            found_measurements.append(measurement)

    if found_measurements:
        print(f"\nDatos meteorológicos para {country_name.upper()}:")
        for measurement in found_measurements:
            print(measurement)
    else:
        print(
            f"\nNo se encontraron datos meteorológicos para el país '{country_name.upper()}'.")
