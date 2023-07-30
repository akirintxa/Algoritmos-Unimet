import requests
import sky_show_functions as skyshow
import sky_analyze_functions as skyanalyze
import sky_search_functions as skysearch
import check

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

# Muestra el menú principal y permite al usuario seleccionar una opción.


def menu(data):
    """Muestra un menú interactivo para consultar información de datos meteorológicos.

    Parameters:
        data (list): Una lista de diccionarios que contiene los datos meteorológicos.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra el menú.
    """
    while True:
        option = input("""
=== MENU PRINCIPAL ===
Seleccione una opción:
    1. Generar reportes
    2. Analizar datos
    3. Filtrar datos
    4. Buscar y consultar información
    0. Salir
                       
""")
        if option == "1":
            skyshow.report_menu(data)

        elif option == "2":
            skyanalyze.analyze_data_menu(data)

        elif option == "3":
            skysearch.filter_data_menu(data)

        elif option == "4":
            skysearch.search_data_menu(data)

        elif option == "0" or option.lower() == "salir":
            print("\nGracias por utilizar esta app!\n")
            break
        else:
            print("*** Por favor elija sólo una de las opciones disponibles.")

# Inicia la app con bienvenida y llamando al menu


def start():
    """Punto de inicio del programa SKYNOW.

    En cada iteración, muestra el título del programa y carga los datos meteorológicos
    desde la API mediante la función 'load_api()'. 
    Luego, invoca la función 'menu()'.


    """
    while True:
        print("""
*==* Bienvenido a SKYNOW *==*
Análisis de datos metereológicos por Idoia Rivas
              """)
        weather_data = load_api()
        menu(weather_data)
        break


start()
