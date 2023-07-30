from alumno import *
from registro import *

registro = Registro([])

persona1 = Alumno("Laura", "Pérez", 15, 987)
persona2 = Alumno("José", "Rodríguez", 20, 654)

alumnos = [
    Alumno("Laura", "Pérez", 15, 987),
    Alumno("José", "Rodríguez", 20, 654),
    Alumno("María", "Márquez", 30, 234),
    Alumno("Miguel", "Soto", 17, 789)
]

for alumno in alumnos:
    registro.agregar_persona(alumno)

print(registro)

# Terminar
