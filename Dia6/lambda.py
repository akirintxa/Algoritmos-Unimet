# sumar = lambda x, y: x + y
# print(sumar(5, 10))

def multiplicar1(x, y):
    return x * y

def multiplicarPorFactor(factor):
    funcionLambda = lambda numero2: factor * numero2
    return funcionLambda

duplicador = multiplicarPorFactor(2)
triplicador = multiplicarPorFactor(3)
print(duplicador(3)) # 6
print(triplicador(3)) # 9

multiplicar2 = lambda x, y : x * y
print(multiplicar1(2, 4))
print(multiplicar2(2, 4))

