class Mes:
    def __init__(self):
        self.nombre = ''
        self.temperatura_minima = 0
        self.temperatura_maxima = 0
    
    def calcular_temperatura_media(self):
        return (self.temperatura_minima + self.temperatura_maxima) / 2
