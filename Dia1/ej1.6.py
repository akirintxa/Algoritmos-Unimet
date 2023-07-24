precio = float(input('Escriba el precio: '))
cantidad = int(input('Escriba la cantidad: '))

subtotal = precio * cantidad
iva = subtotal * 0.16
total = subtotal + iva

print(f'Subtotal: ', subtotal)
print(f'IVA (16%): ', iva)
print(f'Total: ', total)