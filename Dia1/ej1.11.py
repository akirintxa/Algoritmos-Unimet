peso = float(input('Introduzca su peso en Kgs: '))
altura = float(input('Introduzca su altura en Mts: '))

imc = peso / altura ** 2

print(f'Su IMC es {imc:.2f}, para un peso de {peso} y una altura de {altura}')