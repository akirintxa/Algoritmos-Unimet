class Pelicula:
    def __init__(self, titulo, fecha_lanzamiento, genero, calificacion):
        self.titulo = titulo
        self.fecha_lanzamiento = fecha_lanzamiento
        self.genero = genero
        self.calificacion = calificacion

    def __str__(self):
        return f"""
Título: {self.titulo}
Fecha de Lanzamiento: {self.fecha_lanzamiento}
Género: {self.genero}
Calificación: {self.calificacion}"""
