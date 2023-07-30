from Archivo import *


def leer(path):
    data = []
    try:
        archivo = open(path,"r") # Abrimos el archivo
        data = archivo.readlines()
        archivo.close() # Cerramos el archivo
    except Exception:
        print("Ocurrio un error al leer el archivo, verifique que exista y que la ruta este escrita correctamente.")
    return data

def leer2(path):
    data = ""
    try:
        archivo = open(path,"r") # Abrimos el archivo
        data = archivo.read()
        archivo.close() # Cerramos el archivo
    except Exception:
        print("Ocurrio un error al leer el archivo, verifique que exista y que la ruta este escrita correctamente.")
    return data

def sobrescribir(path, nuevaData): # nuevaData debe ser un string. Se vaciara el archivo y se agregara nuevaData
    try:
        archivo = open(path,"w") # Abrimos el archivo
        archivo.write(nuevaData)
        archivo.close() # Cerramos el archivo
    except Exception:
        print("Ocurrio un error al intentar sobrescribir el archivo.")

def agregar(path, nuevaData): # nuevaData debe ser un string. Se agregara nuevaData al final del archivo
    try:
        archivo = open(path,"a") # Abrimos el archivo
        archivo.write(nuevaData)
        archivo.close() # Cerramos el archivo
    except Exception:
        print("Ocurrio un error al intentar agregar en el archivo.")

def vaciar(path):
    sobrescribir(path, "")

def llenarListaDeClientes(data, lista):
    try:
        lineas = []
        lineas = data.split("\n")
        #print(lineas)
        for linea in lineas:
            if "," in linea:
                cliente = linea.split(",")
                #print(cliente)
                lista.append({
                    "nombre": cliente[0],
                    "apellido": cliente[1],
                    "edad": cliente[2]
                })
    except Exception:
        print("Ocurrio un error al intentar llenar la lista.")
    return lista

def agregarCliente(cliente, lista):
    lista.append(cliente)
    return lista

def actualizarArchivoClientes(lista, archivo):
    clientes = ""
    for cliente in lista:
        clientes += "{},{},{}\n".format(cliente["nombre"], cliente["apellido"], cliente["edad"])
    archivo.sobrescribir(clientes)
    
listaDeClientes = []
data = ""
# asociacionDeVecinos.txt
# clientes.txt
archivo = Archivo(input("Ingrese la ruta del archivo: "))
data = archivo.leer2()
print(data)


listaDeClientes = llenarListaDeClientes(data, listaDeClientes)
#print(listaDeClientes)
listaDeClientes = agregarCliente({
    "nombre": "Tony",
    "apellido": "Contreras",
    "edad": "19"
}, listaDeClientes)

#actualizarArchivoClientes(listaDeClientes, archivo)


