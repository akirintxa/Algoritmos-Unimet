contact_list = []

# contact_list = [{"name": "Andres", "phone": "1234567"}]

for i in range(3):
    name = input("Escriba su nombre: ")
    phone = input("Escriba su teléfono: ")

    contact_dict = {"name": name, "phone": phone}
    contact_list.append(contact_dict)

for contact in contact_list:
    print(f"El teléfono de {contact['name']} es {contact['phone']}")
