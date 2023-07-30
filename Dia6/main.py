# Imports
from funciones import *  # Importar TODO

# Funcion main


def main():
    while True:
        print("Hola, soy el bloque de codigo inicial.")
        opciones = ["1", "2"]
        mensaje = "Ingrese opcion 1 para saludar o 2 para salir: "
        opcion = menu(mensaje, opciones)
        if opcion == "1":
            saludar()
        else:
            break


# Llamar a la funcion main
if __name__ == "__main__":
    print(__name__)
    main()
