from alumno import *


def main():
    # Bloque principal
    # Creamos los objetos
    alumno1 = Alumno("Ivan", 9)
    alumno2 = Alumno("Ana", 18)

    # Imprimimos los datos y resultados de cada alumno
    print(alumno1)
    alumno1.resultado()
    alumno2.imprimir_todo()


main()
