import sky_show_functions as skyshow
import check


def search_data_menu(data):
    while True:
        option = input("""
=== MENU 3: BUSCAR DATOS METEREOLÓGICOS ===
Seleccione una opción:
    1. Buscar por fecha
    2. Buscar por variable climática
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
{skyshow.get_weather_variables(data)}""")
                variable_option = input("Introduzca la variable a consultar: ")
                variable_search(data, country_option, variable_option)
            else:
                print(f"""
*** Ese país no está en la lista
Los países disponibles son:
{locations}""")

        elif option == "0" or option.lower() == "salir":
            break

        else:
            print("*** Por favor elija sólo uno de los procedimientos disponibles.")


def date_search(data, country_name, date):
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


def variable_search(data, country_name, variable):
    found = False
    count = 0
    for country_data in data:
        if country_data["location_name"].lower() == country_name.lower():
            for measurement in country_data["location_measurements"]:
                if variable in measurement:
                    print(f"""
Fecha: {measurement['date']}
{variable.title()}: {measurement[variable]}
""")
                    found = True
                    count += 1
            print(
                f"\nSe encontraron {count} mediciones para la variable '{variable.upper()}' de {country_name.upper()}.")
            break
    if not found:
        print("\n*** Revise el nombre de la variable.")
