from edificio import *

edificio1 = Edificio("Los Parques", 1, "Leopoldo",
                     "Caracas", 1080, [1, 2, 3, 4, 5, 6, 7, 8])
edificio2 = Edificio("Caroní", 1, "Asunción", "Caracas",
                     1080, [1, 2])

print("Dirección: ")
edificio1.mostrar_dirección()

print("Clasificación Ed.1: ")
edificio1.clasificación_edificio()

print("Aptos: ")
edificio1.mostrar_apartamentos()

print("Clasificación Ed.2: ")
edificio2.clasificación_edificio()
