class Persona:
    def __init__(self, nombre, apellido, edad):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad

    def cambiar_edad(self, nueva_edad):
        self.edad = nueva_edad

    def mostrar_info(self):
        print(f"""
            Nombre: {self.nombre}
            Apellido: {self.apellido}
            Edad: {self.edad}
        """)

    def metodo(self):
        print("Hola soy un metodo de la clase")

    def getNombre(self):
        return self.nombre

    def getApellido(self):
        return self.apellido

    def getEdad(self):
        return self.edad

    def setNombre(self, nuevo_nombre):
        self.nombre = nuevo_nombre

    def setApellido(self, nuevo_apellido):
        self.apellido = nuevo_apellido

    def setEdad(self, nueva_edad):
        self.edad = nueva_edad
