inicio = int(input('Escribe el inicio de la cuenta: '))
fin = int(input('Escribe el final de la cuenta: '))

# Vertical
for numero in range(inicio, fin + 1):
    print(numero)

# Horizontal
cadena = ""

for numero in range(inicio, fin + 1):
    cadena += str(numero) + " "
print(cadena)
