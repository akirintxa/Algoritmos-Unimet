from cuenta import *
from persona2 import *

persona1 = Persona2("Andrea", "Contreras", 27, 1)

cuenta = Cuenta(persona1, 20)

cuenta.mostrar()  # 20
cuenta.retirar(10)  # 10
cuenta.ingresar(-500)  # 10
cuenta.ingresar(500)  # 510
cuenta.mostrar()  # 510
