class Registro:
    def __init__(self, lista):
        self.listaRecordatorios = lista

    def getListaRecordatorios(self):
        return self.listaRecordatorios

    def mostrar(self):
        for recordatorio in enumerate(self.listaRecordatorios):
            recordatorio.mostrar()

    def agregar(self, recordatorio):
        self.listaRecordatorios.append(recordatorio)

    def borrar(self, opcion):
        for item in self.listaRecordatorios:
            if item.nombre == opcion:
                self.listaRecordatorios.remove(item)
