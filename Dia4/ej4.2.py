product_dict = {"Leche": 2.50, "Pan": 1.50,
                "Huevos": 3.00, "Manzanas": 0.80, "Cereal": 4.50}

product = input("Escriba un producto: ")

if product in product_dict:
    print(
        f"El producto {product} SI existe y su precio es {product_dict[product]}")
else:
    print(f"El producto {product} NO existe")
