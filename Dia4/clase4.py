# semana = ("lun", "mar", "mie", "jue", "vie", "sab", "dom")

# print("\nElementos")
# for dia in semana:
#     print(dia)

# print("\nIndices")
# for i in range(len(semana)):
#     print(semana[i])


# Ejercicio 13
# Tupla de opciones

# menu = (0, 1, 2)

# opcion = int(
#     input("Escoja una opción del menú 1-Saludo, 2-Despedida, 0-Salir: "))
# while opcion not in menu:
#     print("Opción no válida. Intenta de nuevo.")
#     opcion = int(
#         input("Escoja una opción del menú 1-Saludo, 2-Despedida, 0-Salir: "))

# if opcion == 1:
#     print("Hola fulano")
# elif opcion == 2:
#     print("Adios fulano")

# Ejercicio 14
# Sets

# concursantes = {"Maria", "Luis", "Paola", "Antonio", "Laura"}
# ganadores = []

# for persona in concursantes:
#     if len(ganadores) < 3:
#         ganadores.append(persona)

# print(ganadores)

# Diccionarios
# carro = {
#     "marca": "Ford",
#     "anio": 2007,
#     "color": "azul"
# }

# print("\nImprime el diccionario")
# print(carro)

# print("\nImprime un valor de una llave")
# print(carro["color"])
# print(carro.get("color"))
# print(len(carro))

# carro["modelo"] = "Uno"
# print(carro)

# print("\nImprime las llaves")
# for llave in carro:
#     print(llave)

# print("\nImprime las llaves y sus valores")
# for llave in carro:
#     valor = carro[llave]
#     print(llave + ": " + str(valor))

# print("\nImprime las llaves en un tipo de dato de llave")
# llaves = carro.keys()
# print(llaves)

# print("\nConvierto el tipo de dato de llave a lista")
# print(list(carro.keys()))


# Ejercicio 15
# Diccionarios
# productos = {
#     "Leche": 1.50,
#     "Pan": 0.50,
#     "Huevos": 0.75,
#     "Queso": 2.00,
#     "Fruta": 1.00
# }
# mas_caro = 0
# producto_mas_caro = ""


# for producto in productos:
#     valor = productos[producto]
#     if valor > mas_caro:
#         mas_caro = valor
#         producto_mas_caro = producto

# print(f"El producto más caro es {producto_mas_caro} y vale {mas_caro}")

# Estructuras combinadas

# print("Recorrer listas de listas")
# lista_de_estudiantes = [
#     ['Juan', 27, 'Caracas'],
#     ['Maria', 29, 'Valencia'],
#     ['Raul', 30, 'Maracaibo']
# ]

# for estudiante in lista_de_estudiantes:
#     for elemento in estudiante:
#         print(elemento)

print("Recorrer listas de diccionarios")
lista_de_estudiantes = [
    {"nombre": 'Juan',
     "edad": 27,
     "direccion": 'Caracas',
     "notas": [10, 12, 18]
     },

    {"nombre": 'Maria',
     "edad": 29,
     "direccion": 'Valencia',
     "notas": [15, 8, 12]
     }
]

contador = 1
for estudiante in lista_de_estudiantes:
    print("\nEstudiante Nro", contador)
    contador += 1
    llaves = list(estudiante.keys())
    for llave in llaves:
        print(llave, estudiante[llave])
