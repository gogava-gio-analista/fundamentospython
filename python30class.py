class Persona:
    # declaraacion de atributos
    nombre = ""
    apellido = ""
    anionacimiento = 0
    email = ""
    pais = ""

    # metodo constructor
    def __init__(self):
        self.pais = "Argentina"


    def getnombrecompleto(self):
        return f"{self.nombre} {self.apellido}"

    def getedad(self, anioactual):
        return anioactual - self.anionacimiento    