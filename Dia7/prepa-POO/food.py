from product import *

class Food(Product):

    def __init__(self, name, price, quantity, type, expiration_date, calories, weight, packaging):
        super().__init__(name, price, quantity, type, expiration_date, calories)
        self.weight = weight
        self.packaging = packaging

    def __str__(self):
        return f"""
Nombre: {self.name}
Precio: {self.price}
Cantidad: {self.quantity}
Tipo: {self.type}
Fecha de Vencimiento: {self.expiration_date}
Calorias: {self.calories}
Peso: {self.weight}
Empaque: {self.packaging}
"""