from product import *
from food import *
from drink import *
from client import *
from shopping_cart import *

def main():
    producto = Product("Computadora", 500, 5, "Default", "2024/12/26", 435)
    """ print(producto)
    print(producto.calculate_subtotal()) """

    food = Food("Queso", 2.5, 3, "Embutido", "2023/11/26", 100, 100, "Bandeja")
    """ print(food)
    print(food.calculate_subtotal()) """

    bebida = Drink("Santa Teresa", 10, 2, "Alcoholic", "2023/11/26", 0, 500, 0.39)
    """ print(bebida)
    print(bebida.calculate_subtotal()) """

    client = Client("Andres", "Rojas", 353453)
    """ print(client) """

    carrito = ShoppingCart(client)

    carrito.add_product(producto)
    carrito.add_product(bebida)
    carrito.add_product(food)

    """ carrito.show_products()
    print(carrito.calculate_totals()) """

    carrito.calculate_invoice()

main()