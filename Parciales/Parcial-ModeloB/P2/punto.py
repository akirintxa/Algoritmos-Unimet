class Punto:
    def __init__(self, coord_x=0, coord_y=0):
        self.coord_x = coord_x
        self.coord_y = coord_y

    def __str__(self):
        return f"El punto es ({self.coord_x}, {self.coord_y})"

    def cuadrante(self):
        if (self.coord_x > 0) and (self.coord_y > 0):
            print(
                f"El punto ({self.coord_x}, {self.coord_y}) está en el cuadrante I")
        elif (self.coord_x > 0) and (self.coord_y < 0):
            print(
                f"El punto ({self.coord_x}, {self.coord_y}) está en el cuadrante II")
        elif (self.coord_x < 0) and (self.coord_y < 0):
            print(
                f"El punto ({self.coord_x}, {self.coord_y}) está en el cuadrante III")
        elif (self.coord_x < 0) and (self.coord_y > 0):
            print(
                f"El punto ({self.coord_x}, {self.coord_y}) está en el cuadrante IV")
        elif (self.coord_x == 0) and (self.coord_y == 0):
            print(
                f"El punto ({self.coord_x}, {self.coord_y}) está sobre el origen")
        elif (self.coord_x == 0):
            print(
                f"El punto ({self.coord_x}, {self.coord_y}) está sobre el eje X")
        else:
            print(
                f"El punto ({self.coord_x}, {self.coord_y}) está sobre el eje Y")

    def vector(self, punto_q):
        qx = punto_q.coord_x - self.coord_x
        qy = punto_q.coord_y - self.coord_y
        return qx, qy
