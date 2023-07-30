# Abrir archivos

#archivo = open("F:\Clase 9\clientes.txt") # Ruta (path)
archivo = open("clientes.txt") # Ruta relativa(path) # Por defecto asume que es r (Leer)
#archivo2 = open("nuevo_archivo.txt", "x") # Crea el archivo en caso de no existir porque le indicamos que es x (Crear)

# Cerrar archivos

archivo.close()
#archivo2.close()

# Leer archivos

archivo = open("clientes.txt", "r") # Abre el archivo ubicado en la ruta indicada (path) para su lectura porque le indicamos que es r (Leer).
data = archivo.read() # Nos retorna un string con toda la informacion
print(data) # Imprimimos el string que nos retorna read()
archivo.close() # Cerramos el archivo

archivo = open("clientes.txt", "r") 
data = archivo.read(15) # Indicamos la cantidad de caracteres
print(data)
archivo.close()

archivo = open("clientes.txt", "r") 
linea1 = archivo.readline() # Leemos la linea 1
linea2 = archivo.readline() # Leemos la linea 2
print(linea1)
print(linea2)
archivo.close()

archivo = open("clientes.txt", "r") 
for linea in archivo:
    print(linea)
archivo.close()

archivo = open("clientes.txt", "r") 
lista = archivo.readlines()
print(lista)
archivo.close()

# Escribir en archivos

### a
archivo = open("clientes2.txt", "a") # Abrimos el archivo y se indica que agregaremos información
archivo.write("Paola,Sisiruca,35\n") # Agregamos al final del archivo
archivo.close() # Cerramos el archivo

archivo = open("clientes2.txt", "r") # Abrimos el archivo para su lectura
for linea in archivo:
  print(linea)
archivo.close() # Cerramos el archivo

### w

archivo = open("clientes2.txt", "w") # Abrimos el archivo
archivo.write("Paola,Sisiruca,35\n") # Agregamos al final del archivo
archivo.close() # Cerramos el archivo

archivo = open("clientes2.txt", "r") # Abrimos el archivo para su lectura
for linea in archivo:
  print(linea)
archivo.close() # Cerramos el archivo


