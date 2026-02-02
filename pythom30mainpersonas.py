from python30class import Persona
persona1 = Persona()
persona1.nombre = "Juan"
persona1.apellido = "Pérez"
persona1.anionacimiento = 1990
persona1.email = "juan.perez@example.com"
persona1.pais = "eeuu"
print("Nombre completo:", persona1.getnombrecompleto())
print("Edad en 2026:", persona1.getedad(2026))

persona2 = Persona()
persona2.nombre = "María"
persona2.apellido = "Gómez"
persona2.anionacimiento = 1985
persona2.email = "maria.gomez@example.com" 
print("Nombre completo:", persona2.getnombrecompleto())
print("Edad en 2026:", persona2.getedad(2026))

persona3 = Persona()
persona3.nombre = "Luis"
persona3.apellido = "Rodríguez"
persona3.anionacimiento = 2000
persona3.email = "luis.rodriguez@example.com"
print("Nombre completo:", persona3.getnombrecompleto())
print("Edad en 2026:", persona3.getedad(2026))

print (persona1)