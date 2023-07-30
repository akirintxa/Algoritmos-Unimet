class Cuenta:
    def __init__(self, titular, cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    def getTitular(this):
        return this.titular

    def setTitular(this, nuevoTitular):
        this.titular = nuevoTitular

    def getMonto(this):
        return this.monto

    def setMonto(this, nuevoMonto):
        this.monto = nuevoMonto

    def mostrar(this):
        this.titular.mostrar2()
        print("Cantidad: ", this.cantidad)

    def ingresar(self, cantidad):
        if (cantidad > 0):
            self.cantidad += cantidad
        else:
            print("Ingreso un monto invalido.")

    def retirar(self, cantidad):
        if (cantidad > 0):
            self.cantidad -= cantidad
        else:
            print("Ingreso un monto invalido.")
