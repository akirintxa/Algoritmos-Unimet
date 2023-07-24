# numero = 0
# while numero < 10:
#     numero += 1
#     if numero % 2 == 0:
#         continue
#     print(numero)

# ===========================
# while True:
#     entrada = input("Escriba un número o salir: ")
#     if entrada == 'salir':
#         break

#     numero = int(entrada)
#     resultado = numero * 2
#     print(f"El cuadrado de {numero} es {resultado}")

# ===========================
# edad = input("Escriba su edad: ")

# while not edad.isnumeric() or int(edad) < 0 or int(edad) > 100:
#     print('Escriba solo enteros entre 0 y 100')
#     edad = input("Escriba su edad: ")
# print(edad)

# ===========================
# lista_a = ['ene', 'feb', 'mar', 'abr']
# lista_b = lista_a.copy()
# lista_c = lista_a[2:4]
# lista_b.append('may')
# tamano = len(lista_a)
# # lista_a.append = ['may']

# ultimo_item = lista_a.pop()

# print('Lista A', lista_a)
# print('Lista B', lista_b)
# print('Lista C', lista_c)
# print(lista_a[1:3])
# print('El tamano de la lista a es: ', tamano)
# print('Ultimo item: ', ultimo_item)

# ===========================
# Ejercicio 10
# lista_nombres = ['Ana', 'Juan', 'Pepe', 'Laura']
# nombre = input("Escriba el nombre de una persona: ")

# if nombre in lista_nombres:
#     print(f"{nombre} sí está en la lista")
# else:
#     opcion = input(
#         'El nombre no está en la lista. Quiere agregarlo? 1-si 2-no: ')
#     while not (int(opcion) == 1 or int(opcion) == 2):
#         opcion = input(
#             'Elija solo 1-para agregarlo y 2-para salir: ')
#     if int(opcion) == 1:
#         lista_nombres.append(nombre)
#         print(f'Listo. {nombre} ya se agregó a lista')
#         print(lista_nombres)
#     else:
#         print(f'Listo. {nombre} NO se agregó a lista')
#         print(lista_nombres)

# ===========================
# # Ejercicio 11
# lista_estudiantes = ['Ana Flores', 'Juan Soto', 'Pepe Botella', 'Laura Yépez']
# usernames = []

# for estudiante in lista_estudiantes:
#     username = estudiante.lower()
#     username = username.strip()
#     username = username.replace(" ", "_")
#     username = usernames.append(username)

# print(usernames)

# for i in range(11):  # rango del 0 al 10
#     print(i)

# for i in range(5, 11):  # rango del 5 al 10
#     print(i)

# for i in range(0, 11, 2):  # rango del 0 al 10, de 2 en 2
#     print(i)

# for i in range(11, 1, -1):  # rango del 11 al 2
#     print(i)

# # ===========================
# # # Ejercicio 12

# inicio = int(input('Escriba el número desde el cual quiere contar: '))
# final = int(input('Escriba el número hasta el cual quiere contar: '))
# cadena = ""

# for numero in range(inicio, final + 1):
#     cadena += str(numero) + " "
# print(cadena)

# ===========================
# Ejercicio 13

# numero = int(input('Escriba un número: '))
# factorial = 1

# for i in range(1, numero + 1):
#     factorial = factorial*i
# print(f"El factorial de {numero} es {factorial}")
