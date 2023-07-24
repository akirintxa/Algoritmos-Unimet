precio = float(input('Escriba el precio: '))
cantidad = int(input('Escriba la cantidad: '))

subtotal = precio * cantidad
iva = subtotal * 0.16
total = round(subtotal + iva,2)

print(f'Subtotal: {subtotal:.2f}')
print(f'IVA (16%):{iva:.2f}')
print(f'Total: {total:.2f}')