from state import State
from country import Country
import requests
from country import *
from state import *

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
    countries_list = []
    countries_data = load_api(countries_url)

    for country_data in countries_data:
        name = country_data["location_name"]
        capital = country_data["location_capital"]
        population = country_data["population"]
        currency = country_data["currency"]
        language = country_data["main_language"]

        country_obj = Country(name, capital, population, currency, language)
        countries_list.append(country_obj)

        print(country_obj)  # To check

    return countries_list

# Carga los datos de la API de estados


def load_states_data():
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

            print(state_obj)  # To check

    return states_list


def load_states_data():
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

            print(state_obj)  # To check

    return states_list

# Asociar los estados a los países


# Inicia la app con bienvenida y llamando al menu


def start():

    while True:
        print("""
*==* Bienvenido a SKYNOW *==*
Cargando datos...
""")
        load_countries_data()
        load_states_data()

        break


start()
