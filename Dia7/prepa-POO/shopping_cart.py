class ShoppingCart:

    def __init__(self, client):
        self.client = client
        self.product_list = []

    def add_product(self, product):
        self.product_list.append(product)

    def show_products(self):
        for product in self.product_list:
            print(product)

    def calculate_totals(self):
        subtotal = 0
        for product in self.product_list:
            subtotal += product.calculate_subtotal()

        iva = subtotal * 0.16
        total = subtotal + iva

        return subtotal, iva, total
    
    def calculate_invoice(self):
        print(self.client)
        print("")

        print("Nombre - Cantidad - Precio - Subtotal")
        for product in self.product_list:
            product.show_product_for_invoice()

        subtotal, iva, total = self.calculate_totals()
        print("")
        print(f"Subtotal: {subtotal:.2f}$")
        print(f"IVA: {iva:.2f}$")
        print(f"Total: {total:.2f}$")