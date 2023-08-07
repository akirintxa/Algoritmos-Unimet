class Edificio:
    def __init__(self, nombre="", pisos=0, calle="", ciudad="", codigo_postal=0, lista_aptos=[]):
        self.nombre = nombre
        self.pisos = pisos
        self.calle = calle
        self.ciudad = ciudad
        self.codigo_postal = codigo_postal
        self.lista_aptos = lista_aptos

    def mostrar_dirección(self):
        print(f"""
Nombre: {self.nombre}
Calle: {self.calle}
Ciudad: {self.ciudad}
Código Postal: {self.codigo_postal}
""")

    def clasificación_edificio(self):
        if self.pisos*6 <= len(self.lista_aptos):
            print("Edificio Residencial")
        else:
            print("Bloque de Pisos")

    def mostrar_apartamentos(self):
        for i in self.lista_aptos:
            print(i)
