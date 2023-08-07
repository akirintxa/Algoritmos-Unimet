import skynow_show as show
import skynow_graph as graph


def analyze_data_menu(countries_data, states_data, measurements_data):
    while True:
        option = input("""
    === MENU 2: ANALIZAR INFORMACIÓN ===
    Seleccione una opción:
        1. Análisis de superficie y población de los países.
        2. Análisis de superficie y población de los estados.
        3. Análisis de idiomas.
        4. Análisis estadístico de datos meteorológicos.
        5. Graficar.
        0. Regresar o salir
                        
    """)
        if option == "1":
            country_analysis(countries_data)
        elif option == "2":
            state_analysis(countries_data, states_data)
        elif option == "3":
            language_analysis(countries_data)
        elif option == "4":
            weather_analysis(countries_data, measurements_data)
        elif option == "5":
            graph.show_graphs(countries_data, states_data)

        elif option == "0" or option.lower() == "salir":
            break

        else:
            print("\n*** Por favor elija sólo una de las opciones disponibles.")


def country_analysis(countries_data):
    """Realiza el análisis de población y superficie de los países.

    Parameters:
        countries_data (list): Una lista de objetos Country que contiene información de los países.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra los resultados por consola.
    """

    # Obtener los países con la población más alta y más baja
    max_population_country = None
    min_population_country = None
    for country in countries_data:
        if max_population_country is None or country.population > max_population_country.population:
            max_population_country = country
        if min_population_country is None or country.population < min_population_country.population:
            min_population_country = country

    # Obtener los países con la superficie más alta y más baja
    max_area_country = None
    min_area_country = None
    for country in countries_data:
        if max_area_country is None or country.area > max_area_country.area:
            max_area_country = country
        if min_area_country is None or country.area < min_area_country.area:
            min_area_country = country

    # Obtener el promedio de población y superficie de los países
    total_population = 0
    total_area = 0
    num_countries = len(countries_data)
    for country in countries_data:
        total_population += country.population
        total_area += country.area
    average_population = total_population / num_countries
    average_area = total_area / num_countries

    # Mostrar los resultados por consola
    print("\nAnálisis de superficie y población de los países:\n")
    print(
        f"País con mayor población: {max_population_country.name.upper()} - Población: {max_population_country.population}")
    print(
        f"País con menor población: {min_population_country.name.upper()} -  Población: {min_population_country.population}\n")
    print(
        f"País con mayor superficie: {max_area_country.name.upper()} -  Superficie (km²): {max_area_country.area}")
    print(
        f"País con menor superficie: {min_area_country.name.upper()} -  Superficie (km²): {min_area_country.area}\n")
    print(f"Promedio de población de los países: {average_population:.2f}")
    print(f"Promedio de superficie de los países: {average_area:.2f}")


def state_analysis(countries_data, states_data):
    """Realiza un análisis de la población y superficie de los estados de un país.

    Esta función muestra información estadística sobre la población y superficie de los estados
    de un país seleccionado por el usuario.

    Parameters:
        countries_data (list): Una lista de objetos Country que contiene información de los países.
        states_data (list): Una lista de objetos State que contiene información de los estados.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra los resultados del análisis.
    """
    show.show_country_list(countries_data)
    country_option = input("Ingrese el nombre del país: ").lower()

    # Buscar el país en la lista de países
    country = None
    for c in countries_data:
        if c.name.lower() == country_option:
            country = c
            break

    if not country:
        print(f"No se encontró el país '{country_option.upper()}'.")
        return

    # Obtener los estados del país seleccionado
    country_states = []
    for state in states_data:
        if state.country.lower() == country_option:
            country_states.append(state)

    if not country_states:
        print(
            f"No se encontraron estados para el país '{country_option.upper()}'.")
        return

    # Encontrar los estados con la población más alta y más baja
    max_population_state = None
    min_population_state = None
    for state in country_states:
        if max_population_state is None or state.population > max_population_state.population:
            max_population_state = state
        if min_population_state is None or state.population < min_population_state.population:
            min_population_state = state

    # Encontrar los estados con la superficie más alta y más baja
    max_area_state = None
    min_area_state = None
    for state in country_states:
        if max_area_state is None or state.area > max_area_state.area:
            max_area_state = state
        if min_area_state is None or state.area < min_area_state.area:
            min_area_state = state

    # Calcular el promedio de población y superficie de los estados
    total_population = 0
    total_area = 0
    num_states = len(country_states)
    for state in country_states:
        total_population += state.population
        total_area += state.area
    average_population = total_population / num_states
    average_area = total_area / num_states

    # Mostrar los resultados
    print(
        f"\nAnálisis de superficie y población de los estados en {country_option.upper()}:\n")
    print(
        f"Estado con mayor población: {max_population_state.name.upper()} - Población: {max_population_state.population}")
    print(
        f"Estado con menor población: {min_population_state.name.upper()} - Población: {min_population_state.population}\n")
    print(
        f"Estado con mayor superficie: {max_area_state.name.upper()} - Superficie (km²): {max_area_state.area} ")
    print(
        f"Estado con menor superficie: {min_area_state.name.upper()} - Superficie (km²): {min_area_state.area} km²\n")
    print(f"Promedio de población de los estados: {average_population:.2f}")
    print(f"Promedio de superficie de los estados: {average_area:.2f} km²")


def language_analysis(countries_data):
    """Realiza el análisis de idiomas y muestra los países que hablan cada idioma.

    Parameters:
        countries_data (list): Una lista de objetos Country que contiene información de los países.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra los resultados por consola.
    """
    languages_dict = {}

    for country in countries_data:
        language = country.language.lower()
        if language in languages_dict:
            languages_dict[language].append(country.name)
        else:
            languages_dict[language] = [country.name]

    print("\nAnálisis de Idiomas:\n")
    for language, countries in languages_dict.items():
        countries_str = ""
        for country in countries:
            countries_str += country + ", "
        countries_str = countries_str.rstrip(", ")  # Quita la última coma
        print(
            f"Idioma: {language.upper()} - Países que lo hablan: {countries_str}")


def get_mode(values):
    """Calcula la moda de una lista de valores.

    La moda es el valor que aparece con mayor frecuencia en la lista de valores. En caso de empate, puede haber más de una moda.

    Parameters:
        values (list): Una lista de valores numéricos.

    Returns:
        list: Una lista con los valores de la moda (puede ser una lista vacía si no hay moda).
    """
    # Calcula la moda de una lista de valores
    mode_dict = {}
    for value in values:
        if value in mode_dict:
            mode_dict[value] += 1
        else:
            mode_dict[value] = 1
    max_occurrence = max(mode_dict.values())
    mode = [value for value, occurrence in mode_dict.items() if occurrence ==
            max_occurrence]
    return mode


def weather_analysis(countries_data, measurements_data):
    """Realiza un análisis estadístico de datos meteorológicos para un país específico.

        Esta función solicita al usuario que ingrese el nombre de un país para realizar el análisis.
        Luego, filtra los datos de mediciones por la localización ingresada y calcula el promedio, moda,
        máximo y mínimo para las variables climáticas (temperatura, humedad y velocidad del viento) en ese país.

        Parameters:
            measurements_data (list): Una lista de objetos Measurement que contiene información meteorológica.

        Returns:
            None: Esta función no devuelve ningún valor, simplemente muestra los resultados del análisis.
        """
    show.show_country_list(countries_data)
    # Obtener la localización de la cual se desea hacer el análisis
    location = input("Ingrese el país para hacer el análisis: ").lower()

    # Validar que el país ingresado exista
    location_exists = False
    for measurement in measurements_data:
        if measurement.location_name.lower() == location:
            location_exists = True
            break

    if not location_exists:
        print(
            f"No se encontraron datos meteorológicos para el país '{location.upper()}'.")
        return

    # Filtrar los datos de mediciones por la localización ingresada
    location_measurements = []
    for measurement in measurements_data:
        if measurement.location_name.lower() == location:
            location_measurements.append(measurement)

    # Crear diccionarios para almacenar los datos de cada variable climática
    temperature_data = {
        "values": [],
        "average": None,
        "mode": None,
        "maximum": None,
        "minimum": None
    }

    humidity_data = {
        "values": [],
        "average": None,
        "mode": None,
        "maximum": None,
        "minimum": None
    }

    wind_speed_data = {
        "values": [],
        "average": None,
        "mode": None,
        "maximum": None,
        "minimum": None
    }

    # Llenar los valores de las listas en los diccionarios
    for measurement in location_measurements:
        temperature_data["values"].append(measurement.temperature)
        humidity_data["values"].append(measurement.humidity)
        wind_speed_data["values"].append(measurement.wind_speed)

    # Calcular el promedio para cada variable climática
    temperature_data["average"] = sum(
        temperature_data["values"]) / len(temperature_data["values"])
    humidity_data["average"] = sum(
        humidity_data["values"]) / len(humidity_data["values"])
    wind_speed_data["average"] = sum(
        wind_speed_data["values"]) / len(wind_speed_data["values"])

    # Calcular la moda para cada variable climática
    temperature_data["mode"] = get_mode(temperature_data["values"])
    humidity_data["mode"] = get_mode(humidity_data["values"])
    wind_speed_data["mode"] = get_mode(wind_speed_data["values"])

    # Calcular el máximo y mínimo para cada variable climática
    temperature_data["maximum"] = max(temperature_data["values"])
    temperature_data["minimum"] = min(temperature_data["values"])
    humidity_data["maximum"] = max(humidity_data["values"])
    humidity_data["minimum"] = min(humidity_data["values"])
    wind_speed_data["maximum"] = max(wind_speed_data["values"])
    wind_speed_data["minimum"] = min(wind_speed_data["values"])

    # Mostrar los resultados para cada variable climática
    print(
        f"\nAnálisis estadístico de datos meteorológicos para '{location.upper()}':")
    print("\nTemperatura (°C):")
    print(f"Promedio: {temperature_data['average']:.2f}")
    print(f"Moda: {temperature_data['mode']}")
    print(f"Máximo: {temperature_data['maximum']}")
    print(f"Mínimo: {temperature_data['minimum']}")

    print("\nHumedad (%):")
    print(f"Promedio: {humidity_data['average']:.2f}")
    print(f"Moda: {humidity_data['mode']}")
    print(f"Máximo: {humidity_data['maximum']}")
    print(f"Mínimo: {humidity_data['minimum']}")

    print("\nVelocidad del Viento (Km/h):")
    print(f"Promedio: {wind_speed_data['average']:.2f}")
    print(f"Moda: {wind_speed_data['mode']}")
    print(f"Máximo: {wind_speed_data['maximum']}")
    print(f"Mínimo: {wind_speed_data['minimum']}")
