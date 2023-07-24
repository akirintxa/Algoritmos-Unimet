'''
#Piedra, papel o tijera

jugador1 = int(input("Jugador 1 => Escoge 1-piedra, 2-papel o 3-tijera: "))
jugador2 = int(input("Jugador 2 => Escoge 1-piedra, 2-papel o 3-tijera: "))

if jugador1 == jugador2:
    print ("==> Empate")
elif (jugador1 == 1 and jugador2 == 3) or (jugador1 == 2 and jugador2 == 1) or (jugador1 == 3 and jugador2 == 2):
    print ("==> Gana Jugador 1")
else:
    print ("==> Gana Jugador 2")
'''

'''
# Pedir dos números y que haga operaciones matemáticas
num1 = float(input('Introduzca un primer número: '))
num2 = float(input('Introduzca un segundo número: '))

print (f'La suma de {num1} más {num2} es = ', num1 + num2)
print (f'La resta  de {num1} menos {num2} es = ', num1 - num2)
print (f'La multiplicación  de {num1} por {num2} es = ', num1 * num2)
print (f'La división de {num1} entre {num2} es = ', num1 / num2)
print (f'La división entera de {num1} entre {num2} es = ', num1 // num2)
print (f'El módulo  de {num1} entre {num2} es = ', num1 % num2)
print (f'La potenciación  de {num1} a la {num2} es = ', num1 ** num2)

print ("*"*20)
print (f'El valor absoluto de {num1} es = ', abs(num1))
print (f'El valor absoluto de {num2} es = ', abs(num2))

if num1 == num2:
    print (f"{num1} es igual a {num2}")
elif num1 > num2:
    print (f"{num1} es mayor que {num2}")
else:
    print (f"{num2} es mayor que {num1}")
'''

'''
TAREA => Calcula el premio de un juego Ejercicio 7
'''

'''
Ej 8
Revisar si el numero que escribe el usuario es entero


# Opción 1
x = True
while x:
    numero = input("Escriba un número: ")
    if numero.isdigit():
        print (f"{numero} => es entero")
        x = False


# Opción 2
numero = input("Escriba un número: ")
while not numero.isdigit():
    print("Intente de nuevo. Debe ser un número")
    numero = input("Escriba un número: ")
print (f"{numero} => es entero")
'''

'''
Ej 9
Solicitar nombre, ci y edad
Imprimir {nombre} es una persona de CI y de edad {edad}
Validar que el nimbre sean
'''

nombre = input("Escriba su nombre: ")
while not nombre.isalpha():
    print("Intente de nuevo. Debe ser un nombre sin números")
    nombre = input("Escriba su nombre: ")

ci = input("Escriba su cédula: ")
while not ci.isnumeric():
    print("Intente de nuevo. Deben ser solo números")
    ci = input("Escriba su cédula: ")

edad = input("Escriba su edad: ")
while not (edad.isnumeric() and int(edad) > 0 and int(edad) <= 100):
    print("Intente de nuevo. Deben ser solo números y estar entre 0 y 100")
    edad = input("Escriba su cédula: ")

print (f'{nombre} es una persona de CI {ci} y de edad {edad}')
x = True
