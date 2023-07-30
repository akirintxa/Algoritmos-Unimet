class Alumno:
    # inicializamos los atributos
    def __init__(self, nombre, nota):
        self.nombre = nombre
        self.nota = nota

    # funcion para imprimir todos los datos
    def imprimir_todo(self):
        print("Nombre: " + self.nombre)
        print("Nota: ", self.nota)
        self.resultado()

    # funcion para obtener el resultado
    def resultado(self):
        if self.nota < 10:
            print("El alumno ha suspendido.")
        else:
            print("El alumno ha aprobado.")

    # funcion para imprimir los datos
    def imprimir(self):
        print("Nombre: " + self.nombre)
        print("Nota: " + str(self.nota))

    # Metodo __str__()
    def __str__(self):
        return f"Alumno: {self.nombre}. Nota: {self.nota}."
