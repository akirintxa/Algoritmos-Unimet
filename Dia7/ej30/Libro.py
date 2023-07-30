# Clase Padre
class Libro:
    def __init__(self, titulo, autor, anio):
        self.titulo = titulo
        self.autor = autor
        self.anio = anio

    def getTitulo(self):
        return self.titulo

    def conseguir_info(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}"

    def info(self):
        print(f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.anio}")
