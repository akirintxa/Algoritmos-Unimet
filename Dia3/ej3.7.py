while True:
    numero = int(input("Escriba un número entero: "))

    divisores = [1]

    for i in range(2, numero + 1):
        if numero % i == 0:
            divisores.append(i)

    print(f"Los divisores son:  {divisores}")

    if len(divisores) == 2:
        print(f"El número es primo")
    else:
        print(f"El número no es primo")

    opcion = int(input("Escriba 0 para salir y 1 para continuar: "))
    if opcion == 0:
        break
print("Fin del programa")
