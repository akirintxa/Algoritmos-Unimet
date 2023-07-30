class Persona2:
    def __init__(self, nombre="", apellido="", edad=0, dni=0):
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.dni = dni

    def getNombre(self):
        return self.nombre

    def mostrar2(this):
        print("Persona: {} {} \nDNI: {} \nEdad: {}".format(
            this.nombre, this.apellido, this.dni, this.edad))

    def esMayor(self):
        return (self.edad >= 18)

    def esMayor2(self):
        if self.edad >= 18:
            return True
        else:
            return False
