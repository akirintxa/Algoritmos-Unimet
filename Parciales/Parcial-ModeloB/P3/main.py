from tarea import *
from recordatorio import *
from registro import *

mis_recordatorios = Registro([])


while True:
    option = input("""
    === MENU ===
    Seleccione una opción:
        1. Crear un recordatorio
        2. Borrar un recordatorio de la lista
        3. Actualizar un recordatorio
        4. Ver lista de recordatorios
        0. Regresar o salir
                       
""")
    if option == "1":
        nombre = "Salida"
        fecha = "03/08/2023"
        hora = "15:00"
        tareas = ["tarea 1", "tarea 2"]
        recordatorio = Recordatorio(nombre, hora, fecha, tareas)
        mis_recordatorios.agregar(recordatorio)
        mis_recordatorios.mostrar()

    elif option == "2":
        mis_recordatorios.mostrar()
        opcion = input("Escribe el nombre que quieres borrar: ")
        mis_recordatorios.borrar(opcion)
        mis_recordatorios.mostrar

    elif option == "3":
        mis_recordatorios.mostrar()
        opcion = input("Escribe el nombre que quieres modificar: ")
        mis_recordatorios.modificar(opcion)
        mis_recordatorios.mostrar
    elif option == "4":
        mis_recordatorios.mostrar()
    elif option == "0" or option.lower() == "salir":
        break

    else:
        print("*** Por favor elija sólo una de las opciones disponibles.")
