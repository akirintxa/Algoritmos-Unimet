class Carro2:
    def __init__(self, marca, modelo, año, color, número_de_puertas, número_de_pasajeros):
        self.marca = marca
        self.modelo = modelo
        self.año = año
        self.color = color
        self.número_de_puertas = número_de_puertas
        self.número_de_pasajeros = número_de_pasajeros

    def __metodo_privado(self):
        print('Este es un método privado')

    def acelerar(self):
        print('El carro está acelerando.')

    def frenar(self):
        print('El carro está frenando.')
