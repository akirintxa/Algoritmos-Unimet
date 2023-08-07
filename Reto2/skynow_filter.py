import auxiliar
import skynow_show as show


def filter_data_menu(countries_data, states_data, measurements_data):
    while True:
        option = input("""
    === MENU 3: FILTRAR DATOS ===
    Seleccione una opción:
        1. Filtrar estados por población
        2. Filtrar estados por superficie
        0. Regresar o salir
                       
""")
        if option == "1":
            print(
                "\nSe mostrarán los estados de un país cuya población sea mayor o igual a la que se indique")
            show.show_country_list(countries_data)
            country_option = input("Escriba el país a consultar: ")
            population_option = input("Escriba la población: ")
            # Validar que la población ingresada sea un número
            if auxiliar.is_number(population_option):
                filter_state_by_population(
                    countries_data, states_data, country_option, population_option)
            else:
                print("\n*** Debe ingresar un valor numérico para la población.")

        elif option == "2":
            print(
                "\nSe mostrarán los estados de un país cuya superficie esté entre los rangos indicados")
            show.show_country_list(countries_data)
            country_option = input("Escriba el país a consultar: ")
            min_area_option = input("Escriba el área mínima (km²): ")
            max_area_option = input("Escriba el área máxima (km²): ")

            filter_state_by_area(countries_data, states_data, country_option,
                                 min_area_option, max_area_option)

        elif option == "0" or option.lower() == "salir":
            break

        else:
            print("*** Por favor elija sólo una de las opciones disponibles.")


def filter_state_by_population(countries_data, states_data, country_name, population_target):
    """
    Filtra y muestra los estados de un país con población mayor o igual al valor objetivo.

    Parameters:
        countries_data (list): Lista de objetos Country que contiene información de los países.
        states_data (list): Lista de objetos State que contiene información de los estados.
        country_name (str): Nombre del país que se desea filtrar.
        population_target (int): Valor de población objetivo para filtrar los estados.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra los resultados por consola.
    """
    found_country = None
    filtered_states = []

    for country in countries_data:
        if country.name.lower() == country_name.lower():
            found_country = country
            break

    if found_country:
        # Iteramos sobre cada objeto State en states_data.
        for state in states_data:
            if state.country.lower() == country_name.lower() and state.population >= int(population_target):
                filtered_states.append(state)

        if filtered_states:
            print(
                f"\nEstados de {country_name.upper()} con población mayor o igual a {population_target}:")
            for state in filtered_states:
                state.print_state_population()
        else:
            print(
                f"\nNo se encontraron estados en {country_name.upper()} con población mayor o igual a {population_target}.")
    else:
        print(
            f"\nEl país '{country_name.upper()}' no fue encontrado en la lista de países.")


def filter_state_by_area(countries_data, states_data, country_name, min_area_target, max_area_target):
    """
    Filtra y muestra los estados de un país cuya superficie está dentro del rango indicado.

    Parameters:
        countries_data (list): Lista de objetos Country que contiene información de los países.
        states_data (list): Lista de objetos State que contiene información de los estados.
        country_name (str): Nombre del país que se desea filtrar.
        min_area_target (int): Valor mínimo de superficie objetivo para filtrar los estados.
        max_area_target (int): Valor máximo de superficie objetivo para filtrar los estados.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra los resultados por consola.
    """
    found_country = None
    filtered_states = []

    for country in countries_data:
        if country.name.lower() == country_name.lower():
            found_country = country
            break

    if found_country:
        # Validar que min_area_target y max_area_target sean números
        if auxiliar.is_number(min_area_target) and auxiliar.is_number(max_area_target):
            min_area_target = int(min_area_target)
            max_area_target = int(max_area_target)

            # Iteramos sobre cada objeto State en states_data.
            for state in states_data:
                # Validamos que el país y la superficie estén dentro del rango
                if state.country.lower() == country_name.lower() and min_area_target <= int(state.area) <= max_area_target:
                    filtered_states.append(state)

            if filtered_states:
                print(
                    f"\nEstados de {country_name.upper()} cuya superficie está entre {min_area_target} y {max_area_target} km²:")
                for state in filtered_states:
                    state.print_state_area()
            else:
                print(
                    f"\nNo se encontraron estados en {country_name.upper()} dentro del rango de superficie indicado.")
        else:
            print("\n*** Los valores de área deben ser números.")
    else:
        print(
            f"\nEl país '{country_name.upper()}' no fue encontrado en la lista de países.")
