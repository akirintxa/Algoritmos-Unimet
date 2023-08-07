import requests
from country import *
from state import *
from measurement import *

states_url = "https://raw.githubusercontent.com/Andresarl16/API-Retos/main/location-states-api.json"
countries_url = "https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-data-api.json"
measurements_url = "https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json"

# Carga los datos de la API consultada


def load_api(url):
    """Carga los datos de una API desde una URL específica y devuelve los datos en formato JSON.

    Returns:
        dict: Un diccionario que contiene los datos de la API en formato JSON.
    """
    # Se lee la API
    response = requests.get(url)
    # Se guarda la info de la API en una variable, si la lectura es exitosa (status_code = 200)
    api_data = response.json()
    return api_data


# Carga los datos de la API de países
def load_countries_data():
    """Carga los datos de la API de países y los convierte en una lista de objetos Country.

    Esta función utiliza la función 'load_api(url)' para obtener los datos de la API de países desde la URL específica. Luego, convierte los datos en una lista de objetos Country, donde cada objeto contiene información sobre un país.

    Returns:
        list: Una lista de objetos Country que contiene información de los países.
    """
    countries_list = []
    countries_data = load_api(countries_url)

    for country_data in countries_data:
        name = country_data["location_name"]
        capital = country_data["location_capital"]
        population = country_data["population"]
        area = country_data["area"]
        currency = country_data["currency"]
        language = country_data["main_language"]

        country_obj = Country(name, capital, population,
                              area, currency, language)
        countries_list.append(country_obj)

        # print(country_obj)  # To check

    return countries_list

# Carga los datos de la API de estados


def load_states_data():
    """Carga los datos de la API de estados y los convierte en una lista de objetos State.

    Esta función utiliza la función 'load_api(url)' para obtener los datos de la API de estados desde la URL específica. Luego, convierte los datos en una lista de objetos State, donde cada objeto contiene información sobre un estado.

    Returns:
        list: Una lista de objetos State que contiene información de los estados.
    """
    states_list = []
    states_data = load_api(states_url)

    for state_data in states_data:
        country = state_data.get("location_name")
        for city in state_data["location_states"]:
            name = city.get("state_name")
            capital = city.get("state_capital")
            population = city.get("population")
            area = city.get("area")

            state_obj = State(country, name, capital, population, area)
            states_list.append(state_obj)

            # print(state_obj)  # To check

    return states_list

# Carga los datos de la API de datos metereológicos


def load_measurements_data():
    """Carga los datos de la API de mediciones meteorológicas y los convierte en una lista de objetos Measurement.

    Esta función utiliza la función 'load_api(url)' para obtener los datos de la API de mediciones meteorológicas desde la URL específica. Luego, convierte los datos en una lista de objetos Measurement, donde cada objeto contiene información sobre una medición meteorológica.

    Returns:
        list: Una lista de objetos Measurement que contiene información de las mediciones meteorológicas.
    """
    measurements_list = []
    measurements_data = load_api(measurements_url)

    for measure_data in measurements_data:
        country = measure_data.get("location_name")
        for measure in measure_data["location_measurements"]:
            temperature = measure.get("temperature")
            humidity = round(measure.get("humidity")*100, 2)
            wind_speed = measure.get("wind_speed")
            date = measure.get("date")

            measure_obj = Measurement(
                country, temperature, humidity, wind_speed, date)
            measurements_list.append(measure_obj)

            # print(measure_obj)  # To check

    return measurements_list


def start():
    """Inicia la aplicación SKYNOW y carga los datos de las API's de países, estados y mediciones meteorológicas.

        Esta función se ejecuta al inicio de la aplicación y carga los datos necesarios para su funcionamiento desde las API's correspondientes. Utiliza las funciones 'load_countries_data()', 'load_states_data()' y 'load_measurements_data()' para obtener los datos de los países, estados y mediciones meteorológicas respectivamente. Los datos cargados son almacenados en listas de objetos Country, State y Measurement, y luego son retornados.

        Returns:
            tuple: Una tupla que contiene las listas de objetos Country, State y Measurement con la información de los países, estados y mediciones meteorológicas, respectivamente.
        """
    print("""
*==* Bienvenido a SKYNOW *==*
Cargando datos...
""")
    countries_list = load_countries_data()
    states_list = load_states_data()
    measurements_list = load_measurements_data()
    return countries_list, states_list, measurements_list
