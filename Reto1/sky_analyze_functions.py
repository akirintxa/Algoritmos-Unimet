import sky_show_functions as skyshow
import check


def analyze_data_menu(data):
    """Muestra un menú interactivo para analizar los datos meteorológicos de un país.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.

    Returns:
        None: Esta función no devuelve ningún valor, solo muestra las estadísticas
        y los mensajes correspondientes por pantalla.
    """
    while True:
        print("\n=== MENU 2: ANALIZAR DATOS METEREOLÓGICOS ===")
        country_option = input(
            "Escriba el país a consultar (--> 0 para salir): ")
        if country_option == "0":
            break
        else:
            locations = skyshow.get_all_locations(data)
            if check.is_in_list(locations, country_option):
                calculate_weather_stats(data, country_option)
            else:
                print(f"""
*** Ese país no está en la lista
Los países disponibles son:
{locations}""")


def average(sample_list):
    """Calcula el promedio de una lista números.

    Parameters:
        sample_list (list): Una lista de valores numéricos.

    Returns:
        float: El promedio de los valores en la lista, redondeado a 2 decimales.
    """
    average = round(sum(sample_list)/len(sample_list), 2)
    return average


def min_and_max(sample_list):
    """Encuentra el valor mínimo y máximo en una lista de números.

    Parameters:
        sample_list (list): Una lista de valores numéricos.

    Returns:
        tupla: Que contiene el valor mínimo y el valor máximo encontrados
        en la lista.
    """
    max_number = sample_list[0]
    min_number = sample_list[0]
    for number in sample_list:
        if number > max_number:
            max_number = number
        if number < min_number:
            min_number = number
    return min_number, max_number


def mode(sample_list):
    """Encuentra el valor o valores que más se repiten en una lista de números.

    Parameters:
        sample_list (list): Una lista de valores numéricos.

    Returns:
        list or None: Una lista que contiene los valores que más se repiten en la lista.
        Si todos los valores son únicos, se devuelve None.
    """
    repetitions = 0
    mode_number = []

    for i in sample_list:
        n = sample_list.count(i)
        if n > repetitions:
            repetitions = n

    for i in sample_list:
        n = sample_list.count(i)
        if n == repetitions and i not in mode_number:
            mode_number.append(i)

    if len(mode_number) != len(sample_list):
        return mode_number
    else:
        return None


def calculate_weather_stats(data, country_name):
    """Calcula y muestra las estadísticas meteorológicas para un país específico.

    La función busca en los datos 'data' las mediciones para el país 'country_name'
    y calcula el promedio, valor mínimo y máximo, y la moda de temperatura, humedad y velocidad
    del viento. Luego imprime los resultados.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.
        country_name (str): El nombre del país a consultar.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente imprime las estadísticas.
    """
    temperature = []
    humidity = []
    wind_speed = []
    count = 0
    for country_data in data:
        if country_data["location_name"].lower() == country_name.lower():
            for measurement in country_data["location_measurements"]:
                temperature.append(measurement["temperature"])
                humidity.append(measurement["humidity"])
                wind_speed.append(measurement["wind_speed"])
                count += 1

    print(f"""
    Estadísticas para -> {country_name.upper()}
    Total de mediciones encontradas: {count}

    Promedio de temperatura (°C): {average(temperature)}
    Temperatura mínima y máxima (°C):{min_and_max(temperature)}
    Moda de temperatura (°C): {mode(temperature)}

    Promedio de humedad (%): {average(humidity)}
    Humedad mínima y máxima (%):{min_and_max(humidity)}
    Moda de humedad (%): {mode(humidity)}

    Promedio de velocidad del viento (m/s): {average(wind_speed)}
    Velocidad del viento mínima y máxima (m/s):{min_and_max(wind_speed)}
    Moda de velocidad del viento (m/s): {mode(wind_speed)}
    """)
