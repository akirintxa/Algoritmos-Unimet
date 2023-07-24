product_list = [{"name": "Pan", "price": 2.20, "stock": 15},
                {"name": "Azúcar", "price": 3.15, "stock": 23},
                {"name": "Queso", "price": 2.87, "stock": 8}]

option = input("Qué producto quieres buscar: ")

found = False
for product in product_list:
    if option in product["name"]:
        print(f"{option} SI está en la lista")
        print(
            f"Su precio es {product['price']} y quedan {product['stock']} productos")
        found = True
        break
if not found:
    print("El producto no está en la lista")
