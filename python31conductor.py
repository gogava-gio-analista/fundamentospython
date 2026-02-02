from class31coche import Coche
from python32heredar import Deportivo

car = Coche()
car.marca = 'Toyota'
car.modelo = 'Corolla'
car.arrancar()
car.acelerar()
car.acelerar()
car.frenar()
car.getvelocidadmaxima()
print('---')

depor = Deportivo()
depor.arrancar()
depor.acelerar()
depor.turbo()
depor.frenar()
print("Velocidad máxima del deportivo:", depor.getvelocidadmaxima())