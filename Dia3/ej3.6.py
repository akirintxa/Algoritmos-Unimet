lista1 = []
lista2 = []
lista3 = []

for i in range(1, 4):
    num = int(input(f"Introduzca un número {i}: "))
    lista1.append(num)

for i in range(1, 4):
    num = int(input(f"Introduzca un número {i}: "))
    lista2.append(num)

for num in lista1:
    if not (num in lista3):
        lista3.append(num)

for num in lista2:
    if not (num in lista3):
        lista3.append(num)

print(lista3)
