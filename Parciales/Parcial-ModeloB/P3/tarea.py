class Tarea():
    def __init__(self, nombre) -> None:
        self.nombre = nombre

    def __str__(self):
        return f"TAREA: {self.nombre}"

    def info(self):
        return f"{self.nombre}"
