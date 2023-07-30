class Product:

    def __init__(self, name, price, quantity, type, expiration_date, calories):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.type = type
        self.expiration_date = expiration_date
        self.calories = calories

    def __str__(self):
        return f"""
Nombre: {self.name}
Precio: {self.price}
Cantidad: {self.quantity}
Tipo: {self.type}
Fecha de Vencimiento: {self.expiration_date}
Calorias: {self.calories}
"""
    
    def calculate_subtotal(self):
        return self.price * self.quantity
    
    def show_product_for_invoice(self):
        print(f"{self.name} - {self.quantity} - {self.price:.2f}$ - {self.calculate_subtotal():.2f}$")