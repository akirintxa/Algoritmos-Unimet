from product import *

class Drink(Product):

    def __init__(self, name, price, quantity, type, expiration_date, calories, volume, alcoholic_degree):
        super().__init__(name, price, quantity, type, expiration_date, calories)
        self.volume = volume
        self.alcoholic_degree = alcoholic_degree

    def __str__(self):
        return f"""
Nombre: {self.name}
Precio: {self.price}
Cantidad: {self.quantity}
Tipo: {self.type}
Fecha de Vencimiento: {self.expiration_date}
Calorias: {self.calories}
Volumen: {self.volume}
Grado Alcoholico: {self.alcoholic_degree}
"""
    
    def calculate_subtotal(self):
        if self.type == "Alcoholic":
            semi_subtotal = self.price * self.quantity
            extra = semi_subtotal * self.alcoholic_degree
            subtotal = semi_subtotal + extra
            return subtotal
        elif self.type == "Normal":
            semi_subtotal = self.price * self.quantity
            discount = semi_subtotal * 0.15
            subtotal = semi_subtotal - discount
            return subtotal
        else:
            return self.price * self.quantity