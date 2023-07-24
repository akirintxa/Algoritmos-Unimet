while True:
    numero = int(input("Escriba un número entero: "))

    divisores = [1]

    for i in range(2, numero):
        if numero % i == 0:
            divisores.append(i)

    print(f"Los divisores son:  {divisores}")

    sumatoria = sum(divisores)
    if sumatoria == numero:
        print(
            f"El número {numero} es perfecto, porque la sumatoria de sus dígitos es {sumatoria}")
    else:
        print(
            f"El número {numero} no es perfecto, , porque la sumatoria de sus dígitos es {sumatoria}")

    opcion = int(input("Escriba 0 para salir y 1 para continuar: "))
    if opcion == 0:
        break
print("Fin del programa")
