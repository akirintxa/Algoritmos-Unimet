# Declarar en un archivo de Python la siguiente lista de Strings:
# color_list = ["red", "green", "blue", "yellow", "purple", "pink", "brown", "black", "white"]
# Posteriormente, recorrer la lista e imprimir todos los colores uno por uno utilizando un bucle for

color_list = ["red", "green", "blue", "yellow",
              "purple", "pink", "brown", "black", "white"]

# Opción 1
print("Opción 1")
for color in color_list:
    print(color)

# Opción 2
print("Opción 2")
for i in range(1, len(color_list)):
    print(color_list[i])
