from pelicula import *
import funciones

peliculas = [
    {"titulo": "Oppenheimer", "fecha_lanzamiento": "2023-07-21", "genero":
     "Historia", "calificacion": 8.7},
    {"titulo": "Barbie", "fecha_lanzamiento": "2023-07-21", "genero":
     "Comedia", "calificacion": 7.0},
    {"titulo": "Mario Bros", "fecha_lanzamiento": "2023-04-05", "genero":
     "Animación", "calificacion": 9.6},
    {"titulo": "Guardianes de la Galaxia Vol. 3", "fecha_lanzamiento":
     "2023-05-05", "genero": "Historia", "calificacion": 9.0},
    {"titulo": "Calabozos y dragones: Honor entre ladrones",
     "fecha_lanzamiento": "2023-03-31", "genero": "Comedia", "calificacion":
     8.4},
]


data_peliculas = funciones.leer_data(peliculas)
funciones.menu(data_peliculas)
