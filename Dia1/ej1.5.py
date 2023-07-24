'''
Pedir al usuario 2 números y después calcular el divmod
'''

numerador = int(input('Número 1: '))
denominador = int(input('Número 1: '))

div, mod = divmod(numerador, denominador)

print(f'La división entera es: {div}')
print(f'El módulo de la división es: {mod}')