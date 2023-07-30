def factorial(number):
    if number > 1:
        return number * factorial(number - 1)
    else:
        return 1

def start():
    number = int(input("Introduza un número: "))
    value = factorial(number)
    print(value)

start()