class Coche:
    def __init__(self):
        self.marca = ''
        self.modelo = ''
        self.velocidad = 0
        self.estado = False

    def arrancar(self):
        self.estado = True
        print("El coche ha arrancado.")
    
    def detener(self):
        self.estado = False
        print("El coche se ha detenido.")

    def acelerar(self):
        if self.estado:
            self.velocidad += 10
            print(f"El coche ha acelerado. Velocidad actual: {self.velocidad} km/h")
        else:
            print("El coche está detenido. No puede acelerar.")

    def frenar(self):
        if self.estado and self.velocidad >= 10:
            self.velocidad -= 10
            print(f"El coche ha frenado. Velocidad actual: {self.velocidad} km/h")
        elif self.velocidad < 10:
            self.velocidad = 0
            print("El coche se ha detenido por completo.")
        else:
            print("El coche está detenido. No puede frenar.")

    def getvelocidadmaxima(self):
        return 180