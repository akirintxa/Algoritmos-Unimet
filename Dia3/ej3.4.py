numeros = []
suma = 0
for i in range(1, 6):
    num = int(input(f"Introduzca un número {i}: "))
    numeros.append(num)
    suma += num

print('Los números son:', numeros)
print('La suma de los números es: ', suma)
print('La suma de los números es (usando sum): ', sum(numeros))
