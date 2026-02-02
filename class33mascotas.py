class Mascota:
    def __init__(self):
        self.nombre = ""
        self.anioNacimiento = 0
        self.anioadopcion = 0
        self.tipo = ""

    def anio_cuando_adoptaron(self):
        return self.anioadopcion - self.anioNacimiento