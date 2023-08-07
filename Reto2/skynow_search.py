import skynow_show as show
import auxiliar


def search_data_menu(countries_data, states_data, measurements_data):
    while True:
        option = input("""
    === MENU 4: BUSCAR INFORMACIÓN ===
    Seleccione una opción:
        1. Búsqueda por fecha
        2. Búsqueda por variables climáticas
        3. Búsqueda de información de un estado
        0. Regresar o salir
                        
    """)
        if option == "1":
            show.show_country_list(countries_data)
            country_option = input("Escriba el país a consultar: ")
            locations = show.get_all_countries(countries_data)
            if auxiliar.is_in_list(locations, country_option):
                date_option = input(
                    "Introduzca la fecha en formato AAAA/MM/DD: ")
                date_search(countries_data, country_option,
                            date_option, measurements_data)
            else:
                print(f"*** Ese país no está en la lista")

        elif option == "2":
            show.show_country_list(countries_data)
            country_option = input("Escriba el país a consultar: ")
            locations = show.get_all_countries(countries_data)
            if auxiliar.is_in_list(locations, country_option):
                variable_option = input("""
Seleccione una variable climática:
    1. Temperatura (°C)
    2. Humedad (%)
    3. Velocidad del viento (Km/h)
""")
                if variable_option in ["1", "2", "3"]:
                    value_option = input(
                        "Introduzca el valor de la variable climática: ")
                    climate_variable_search(
                        countries_data, country_option, variable_option, value_option, measurements_data)
                else:
                    print("\n*** Opción inválida. Por favor, elija una opción válida.")
            else:
                print(f"*** Ese país no está en la lista")

        elif option == "3":
            show.show_country_list(countries_data)
            country_option = input("Escriba el país a consultar: ")
            locations = show.get_all_countries(countries_data)
            if auxiliar.is_in_list(locations, country_option):
                state_option = input("Escriba el estado a consultar: ")
                state_search_binary(states_data, country_option, state_option)
            else:
                print(f"*** Ese país no está en la lista")

        elif option == "0" or option.lower() == "salir":
            break

        else:
            print("\n*** Por favor elija sólo una de las opciones disponibles.")


def date_search(countries_data, country_option, date_option, measurements_data):
    """Realiza una búsqueda de datos meteorológicos por fecha.

    Parameters:
        countries_data (list): Una lista de objetos Country que contiene información de los países.
        country_option (str): El país ingresado por el usuario para la búsqueda.
        date_option (str): La fecha ingresada por el usuario en formato AAAA/MM/DD.
        measurements_data (list): Una lista de objetos Measurement que contiene información meteorológica.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra los datos meteorológicos o un mensaje informativo.
    """
    if not auxiliar.is_valid_date(date_option):
        print("\n*** Formato de fecha inválido. Debe ser AAAA/MM/DD.")
        return

    if auxiliar.is_in_list(show.get_all_countries(countries_data), country_option):
        found_measurements = []

        # Buscar los datos meteorológicos que coincidan con la ubicación y la fecha especificadas por el usuario.
        for measurement in measurements_data:
            if measurement.location_name.lower() == country_option.lower() and measurement.date == date_option:
                found_measurements.append(measurement)

        if found_measurements:
            print(
                f"\nDatos meteorológicos para {country_option.upper()} en la fecha {date_option}:")
            for measurement in found_measurements:
                print(measurement)
        else:
            print(
                f"\nNo se encontraron datos meteorológicos para {country_option.upper()} en la fecha {date_option}.")
    else:
        print(
            f"\nEl país '{country_option.upper()}' no fue encontrado en la lista de países.")


def climate_variable_search(countries_data, country_option, variable_option, value_option, measurements_data):
    """Realiza una búsqueda de datos meteorológicos por variables climáticas.

    Parameters:
        countries_data (list): Una lista de objetos Country que contiene información de los países.
        country_option (str): El país ingresado por el usuario para la búsqueda.
        variable_option (str): La opción de variable climática ingresada por el usuario.
        value_option (str): El valor de la variable climática ingresado por el usuario.
        measurements_data (list): Una lista de objetos Measurement que contiene información meteorológica.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra los datos meteorológicos o un mensaje informativo.
    """
    variable_mapping = {
        "1": "temperature",
        "2": "humidity",
        "3": "wind_speed"
    }

    if variable_option in variable_mapping:
        variable_name = variable_mapping[variable_option]
        found_measurements = []

        # Convertir el valor ingresado por el usuario a un número (float o int)
        try:
            value_option = float(value_option)  # Intentar convertir a float
        except ValueError:
            print(
                "\n*** Valor inválido. Debe ingresar un número para la variable climática.")
            return
        # Buscar los datos meteorológicos que coincidan con la ubicación y la variable climática especificadas por el usuario.
        for measurement in measurements_data:
            if measurement.location_name.lower() == country_option.lower():
                if variable_name == "temperature":
                    if measurement.temperature == value_option:
                        found_measurements.append(measurement)
                elif variable_name == "humidity":
                    if measurement.humidity == value_option:
                        found_measurements.append(measurement)
                elif variable_name == "wind_speed":
                    if measurement.wind_speed == value_option:
                        found_measurements.append(measurement)

        if found_measurements:
            print(
                f"\nDatos meteorológicos para {country_option.upper()} con {variable_name} igual a {value_option}:")
            for measurement in found_measurements:
                print(measurement)
        else:
            print(
                f"\nNo se encontraron datos meteorológicos para {country_option.upper()} con {variable_name} igual a {value_option}.")
    else:
        print(
            "\n*** Opción de variable climática inválida. Por favor, elija una opción válida.")


def state_search_iterative(states_data, country_option, state_option):
    """Realiza la búsqueda de información de un estado específico.

    Parameters:
        states_data (list): Una lista de objetos State que contiene información de los estados.
        country_option (str): El nombre del país para el cual se desea buscar el estado.
        state_option (str): El nombre del estado que se desea buscar.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra la información del estado si es encontrado.
    """
    found_state = None

    # Buscar el estado en la lista de estados que coincida con el país y el nombre de estado especificados
    for state in states_data:
        if state.country.lower() == country_option.lower() and state.name.lower() == state_option.lower():
            found_state = state
            break

    if found_state:
        print(f"\nInformación del estado {found_state.name}:")
        print(f"Estado: {found_state.name}")
        print(f"Capital: {found_state.capital}")
        print(f"Población: {found_state.population}")
        print(f"Area (km²): {found_state.area}")
    else:
        print(
            f"\nEl estado '{state_option}' no fue encontrado en la lista de estados para el país '{country_option}'.")


def state_search_binary(states_data, country_option, state_option):
    """Realiza la búsqueda de información de un estado específico utilizando búsqueda binaria.

    Parameters:
        states_data (list): Una lista ORDENADA de objetos State que contiene información de los estados.
        country_option (str): El nombre del país para el cual se desea buscar el estado.
        state_option (str): El nombre del estado que se desea buscar.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra la información del estado si es encontrado.
    """
    # Ordenar la lista de estados alfabéticamente por el nombre del estado
    states_data.sort(key=lambda state: state.name.lower())

    # Realizar la búsqueda binaria en la lista de estados
    found_state = auxiliar.binary_search(states_data, state_option.lower())

    # Verificar que el estado pertenezca al país especificado
    if found_state and found_state.country.lower() == country_option.lower():
        print(f"\nInformación del estado {found_state.name.upper()}:")
        print(f"Estado: {found_state.name}")
        print(f"Capital: {found_state.capital}")
        print(f"Población: {found_state.population}")
        print(f"Area (km²): {found_state.area}")
    else:
        print(
            f"\nEl estado '{state_option}' no fue encontrado en la lista de estados para el país '{country_option.upper()}'.")
