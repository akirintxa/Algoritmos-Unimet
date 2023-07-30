def saludar():
    print("¡Hola!")


def menu(mensaje, opciones):
    print(__name__)
    while True:
        opcion = input(mensaje)
        if opcion in opciones:
            return opcion
        else:
            print("Debe ingresar una opción válida.")


if __name__ == "__main__":
    print("Entra en funciones")
    # No va a entrar porque no es el primer archivo en ejecutarse
