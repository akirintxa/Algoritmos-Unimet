# # Ejercicio 18

# def print_output(output):
#     print(output)


# print_output("Este es el valor de output")

# # Ejercicio 19 y 20
# def factorial(num):
#     factorial = 1
#     for i in range(1, num + 1):
#         factorial *= i
#     return factorial


# print(factorial(5))

import requests

# Valida que la respuesta sea exitosa cuando es 200
# respuesta = requests.get(
#     'https://raw.githubusercontent.com/Andresarl16/API-Retos/main/locations-api.json')
# if respuesta.status_code == 200:
#     data = respuesta.json()
#     print(type(data))  # lista
# else:
#     print("Error", respuesta.status_code)

# while True:
#     try:
#         num = int(input("Escriba un número: "))
#         break
#     except Exception as error:
#         print("Error, debe escribir un número")
# print(num)

# while True:
#     try:
#         decimal = float(input("Escriba un decimal: "))
#         break
#     except Exception as error:
#         print("Error, debe escribir un decimal")
#         print(error)
# print(decimal)

# Ejercicio
nombres = ["Andrea", "Daniela", "Pedro", "Juan", "Gabriel"]
while True:
    try:
        indice = int(input("Escriba el indice del nombre a consultar: "))
        print(nombres[indice])
        break
        # No hace falta esta validación adicional
        # if indice <= len(nombres)-1:
        #     print(nombres[indice])
        #     break
    except Exception as e:
        print(e)
        print(type(e))
