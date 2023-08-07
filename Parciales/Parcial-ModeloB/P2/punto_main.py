from punto import *


def start():
    while True:
        x = int(input("Escriba la coordenada x: "))
        y = int(input("Escriba la coordenada y: "))

        punto = Punto(x, y)
        punto.cuadrante()

        opcion = input("1: Continuar, 0: Salir ")
        if opcion == "0":
            break


def start2():
    while True:
        x1 = int(input("Escriba la x del punto 1: "))
        y1 = int(input("Escriba la y del punto 1: "))

        punto1 = Punto(x1, y1)

        x2 = int(input("Escriba la x del punto 2: "))
        y2 = int(input("Escriba la y del punto 2: "))

        punto2 = Punto(x2, y2)

        print("Se muestra el punto resultante (x2-x1, y2-y1)")
        print(punto1.vector(punto2))

        opcion = input("1: Continuar, 0: Salir ")
        if opcion == "0":
            break


start2()
