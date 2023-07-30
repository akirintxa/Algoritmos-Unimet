from registro import *
from persona2 import *
lista = [Persona2("Andrea", "Contreras", 27, 1),
         Persona2("Andres", "Gomez", 24, 2)]
registro = Registro([])
for persona in lista:
    registro.agregarPersona(persona)
# persona1 = Persona2("Andrea", "Contreras", 27, 1)
# persona2 = Persona2("Andres", "Gomez", 24, 2)


registro.mostrar()
# print(persona1.esMayor())
