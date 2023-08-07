from pelicula import *


def leer_data(peliculas):
    lista_peliculas = []
    for pelicula in peliculas:
        titulo = pelicula["titulo"]
        fecha_lanzamiento = pelicula["fecha_lanzamiento"]
        genero = pelicula["genero"]
        calificacion = pelicula["calificacion"]

        pelicula_obj = Pelicula(
            titulo, fecha_lanzamiento, genero, calificacion)
        lista_peliculas.append(pelicula_obj)
    return lista_peliculas


def ver_peliculas(peliculas):
    for pelicula in peliculas:
        print(pelicula)


def buscar_por_genero(peliculas):
    genero_buscado = input("Ingrese el género que desea buscar: ").lower()
    peliculas_encontradas = []

    for peli in peliculas:
        if peli.genero.lower() == genero_buscado:
            peliculas_encontradas.append(peli)

    if peliculas_encontradas:
        print(
            f"\nLas películas encontradas del género {genero_buscado.upper()} son:")
        for peli in peliculas_encontradas:
            print(peli)
    else:
        print(
            f"\nNo se encontraron películas del género {genero_buscado.upper()}.")


def buscar_por_rango(peliculas):
    min_buscado = input(
        "Ingrese la calificación mínima de las películas a buscar: ")
    max_buscado = input(
        "Ingrese la calificación máxima de las películas a buscar: ")

    try:
        min = float(min_buscado)  # Intentar convertir a float
        max = float(max_buscado)
    except ValueError:
        print("\n*** Valor inválido. Debe ingresar solo números.")

    peliculas_encontradas = []

    if min > max:
        print("\n*** Valor inválido. El valor mínimo debe ser menor que el máximo.")
    else:
        for peli in peliculas:
            if peli.calificacion >= min and peli.calificacion <= max:
                peliculas_encontradas.append(peli)

        if peliculas_encontradas:
            print(
                f"\nLas películas encontradas con calificación entre {min} y {max} son:")
            for peli in peliculas_encontradas:
                print(peli)
        else:
            print(
                f"\nNo se encontraron películas en ese rango de calificación")


def menu(data_peliculas):
    while True:
        option = input("""
=== CINE IDOIA ===
Seleccione una opción:
    1. Ver películas disponibles
    2. Buscar películas por género
    3. Buscar películas con rango de calificación:
    0. Salir
                       
""")
        if option == "1":
            ver_peliculas(data_peliculas)

        elif option == "2":
            buscar_por_genero(data_peliculas)

        elif option == "3":
            buscar_por_rango(data_peliculas)

        elif option == "0" or option.lower() == "salir":
            print("\nGracias por utilizar la app!\n")
            break
        else:
            print("*** Por favor elija sólo una de las opciones disponibles.")
