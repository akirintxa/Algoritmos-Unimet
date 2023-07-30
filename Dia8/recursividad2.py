def sumatoria_iterativo(numero, total):
    inicio = numero  # Inicia en numero
    fin = 0  # No se incluye asi que llega hasta 0
    step = -1  # Va de 1 en 1 decreciendo
    # total = 0 # Resultado suma
    for i in range(inicio, fin, step):
        print("Total ANTES: ", total)
        print("Valor a sumar: ", i)
        total += i  # Sumamos i al total
        print("Total DESPUES: ", total, "\n")
    return total


def sumatoria_recursivo(numero, llamada):
    print("\nllamada numero: ", llamada)
    print(" Numero que recibe la llamada: ", numero)
    if numero == 0:
        print("\nPUNTO DE QUIEBRE ENCONTRADO")
        print("Numero es 0.")
        print("Nos empezamos a regresar.")
        return 0
    else:
        llamada += 1
        siguiente_numero = numero - 1
        return numero + sumatoria_recursivo(siguiente_numero, llamada)


numero = 4
llamada = 1
total = 0
print("ANTES")
print(total)
print()

# Iterativo
# total = sumatoria_iterativo(numero, total)
# Recursivo
total = sumatoria_recursivo(numero, llamada)

print()
print("DESPUES")
print(total)
# 4 + 3 + 2 + 1 + 0
