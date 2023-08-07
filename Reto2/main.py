import skynow_show as skyshow
import skynow_analysis as skyanalyze
import skynow_search as skysearch
import skynow_filter as skyfilter
import start
import local_data  # Cuando no hay internet

countries = []
states = []
measurements = []

# Muestra el menú principal y permite al usuario seleccionar una opción.


def menu(countries, states, measurements):
    """Muestra un menú interactivo para consultar información de datos meteorológicos.

    Parameters:
        data (list): 

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
            skyshow.report_menu(countries, states, measurements)

        elif option == "2":
            skyanalyze.analyze_data_menu(countries, states, measurements)

        elif option == "3":
            skyfilter.filter_data_menu(countries, states, measurements)

        elif option == "4":
            skysearch.search_data_menu(countries, states, measurements)

        elif option == "0" or option.lower() == "salir":
            print("\nGracias por utilizar SKYNOW!\n")
            break
        else:
            print("*** Por favor elija sólo una de las opciones disponibles.")


countries, states, measurements = local_data.start()
# countries, states, measurements = start.start()
menu(countries, states, measurements)
