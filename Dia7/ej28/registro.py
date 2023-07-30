class Registro:
    def __init__(self, lista):
        self.listaPersonas = lista

    def getListaPersonas(self):
        return self.listaPersonas

    def mostrar(self):
        for persona in self.listaPersonas:
            persona.mostrar2()
            print(persona.getNombre())

    def agregarPersona(self, persona):
        self.listaPersonas.append(persona)
