import Ejercicio8_1

def menu():
    print(f"""
Bienvenido al programa de algoritmos recursivos, cual quieres probar
1.- Contar de 1 hasta n
2.- Ver Menu Recursivo
3.-
4.-
5.- 
          """)
    
    option = int(input("Seleccione una opcion: "))

    if option == 1:
        Ejercicio8_1.start()
    elif option == 2:
        """ menu() """
        print("No disponible")

    print("Introduce 1 para continuar usando el programa y 0 para terminar")
    number = int(input("Introduce 0 o 1: "))
    if number == 1:
        menu()


def main():
    menu()
    print("Termino el programa")

main()