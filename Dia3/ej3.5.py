lista1 = []
lista2 = []

for i in range(1, 4):
    num = int(input(f"Introduzca un número {i}: "))
    lista1.append(num)

for i in range(1, 4):
    num = int(input(f"Introduzca un número {i}: "))
    lista2.append(num)

# print("Lista 1: ", lista1)
# print("Lista 2: ", lista2)
# print("Lista Combinada: ", lista1 + lista2)

print(f"""
Lista 1: {lista1}
Lista 2: {lista2}
Lista Combinada: {lista1 + lista2}
""")
