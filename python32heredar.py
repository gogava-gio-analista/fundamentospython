from class31coche import Coche

class Deportivo(Coche):
    def turbo(self):
        self.velocidad += 100
        print(f"El coche deportivo ha activado el turbo. Velocidad actual: {self.velocidad} km/h")

    def acelerar(self):
        self.velocidad += 40
        print(f"El coche deportivo ha acelerado. Velocidad actual: {self.velocidad} km/h")

    def getvelocidadmaxima(self):
        velocidadcoche = super().getvelocidadmaxima()
        return velocidadcoche + 120