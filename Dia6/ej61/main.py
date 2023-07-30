from persona import *


def main():
    lista_personas = [
        Persona("Gloria", "Rivas", 30, 1.70, 70),
        Persona("Manuel", "Soto", 33, 1.78, 85),
        Persona("Raúl", "López", 15, 1.93, 90)
    ]

    for persona in lista_personas:
        # print(persona.getName())
        # print(persona.lastname)
        # print(persona.getFullname())
        # print(persona.calculate_bmi())
        print(persona.is_adult())
        print(persona)  # es igual a print(str(persona))


main()
