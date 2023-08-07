import matplotlib.pyplot as plt


def plot_state_area(states_data):
    """Genera un gráfico de barras para visualizar la superficie de los estados.

    Parameters:
        states_data (list): Una lista de objetos State que contiene información de los estados.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra el gráfico.
    """
    # state_names = [state.name for state in states_data]
    state_names = []
    for state in states_data:
        state_names.append(state.name)

    # state_areas = [state.area for state in states_data]
    state_areas = []
    for state in states_data:
        state_areas.append(state.area)

    plt.figure(figsize=(10, 6))
    plt.bar(state_names, state_areas, color=("green"))
    plt.xlabel('Estados')
    plt.ylabel('Superficie (km²)')
    plt.title('Superficie de los Estados')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def plot_state_population(states_data):
    """Genera un gráfico de barras para visualizar la población de los estados.

    Parameters:
        states_data (list): Una lista de objetos State que contiene información de los estados.

    Returns:
        None: Esta función no devuelve ningún valor, simplemente muestra el gráfico.
    """
    # state_names = [state.name for state in states_data]
    state_names = []
    for state in states_data:
        state_names.append(state.name)

    # state_population = [state.population for state in states_data]
    state_population = []
    for state in states_data:
        state_population.append(state.population)

    plt.figure(figsize=(10, 6))
    plt.bar(state_names, state_population, color=("orange"))
    plt.xlabel('Estados')
    plt.ylabel('Población')
    plt.title('Población de los Estados')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.show()


def show_graphs(countries_data, states_data):
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

    while True:
        option = input("""
        === MENU 5: GRAFICAR ===
        Seleccione una opción:
            1. Superficie de los estados.
            2. Población de los estados.
            0. Regresar o salir

        """)
        if option == "1":
            plot_state_area(country_states)
        elif option == "2":
            plot_state_population(country_states)
        elif option == "0" or option.lower() == "salir":
            break
        else:
            print("\n*** Por favor elija sólo una de las opciones disponibles.")
