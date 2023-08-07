class Recordatorio():
    def __init__(self, nombre, hora, fecha, tareas) -> None:
        self.nombre = nombre
        self.fecha = fecha
        self.hora = hora
        self.tareas = tareas

    def mostrar(self):
        print(f"""
        Nombre: {self.nombre}
        Fecha: {self.fecha}
        Hora: {self.hora}
        Tares: {self.tareas}
        """)
