'''
nombre = input('Escribe tu nombre: ')
apellido = input('Escribe tu apellido: ')
carrera = input('Escribe tu carrera: ')

print (f'Opcion A => {nombre} {apellido}, estudiante de {carrera}')

print ('Opcion B => {} {}, estudiante de {}'.format(nombre,apellido, carrera))

print ('Opcion C')
print (nombre, apellido, carrera)

'''

'''
num1 = float(input('Introduzca un primer número: '))
num2 = float(input('Introduzca un segundo número: '))

print (f'La suma de {num1} más {num2} es = ', num1 + num2)
print (f'La resta  de {num1} menos {num2} es = ', num1 - num2)
print (f'La multiplicación  de {num1} por {num2} es = ', num1 * num2)
print (f'La división de {num1} entre {num2} es = ', num1 / num2)
print (f'La división entera de {num1} entre {num2} es = ', num1 // num2)
print (f'El módulo  de {num1} entre {num2} es = ', num1 % num2)
print (f'La potenciación  de {num1} a la {num2} es = ', num1 ** num2)
'''

fecha = int(input('Escriba su fecah de nacimiento: '))

adulto = fecha + 18

print(f'En {adulto} cumple su mayoría  de edad')