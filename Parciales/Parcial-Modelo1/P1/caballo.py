class Caballo():
    def __init__(self, nombre_caballo, nombre_jockey) -> None:
        self.nombre_caballo = nombre_caballo
        self.nombre_jockey = nombre_jockey

    def __str__(self):
        return f"(Caballo: {self.nombre_caballo}. Jockey: {self.nombre_jockey})"
