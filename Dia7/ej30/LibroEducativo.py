from Libro import *
# Clase hijo


class LibroEducativo(Libro):
    def __init__(self, titulo, autor, anio, tema):
        super().__init__(titulo, autor, anio)
        self.tema = tema

    def info(self):
        super().info()
        print(f"Tema: {self.tema}")

    def pedir_info(self):
        datos = super().conseguir_info()
        titulo = super().getTitulo()
        print(datos + f", Tema: {self.tema}")
