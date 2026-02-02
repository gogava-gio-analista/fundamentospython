from class33mascotas import Mascota

listamascotas = []
for i in range(3):
    mascota = Mascota()
    mascota.nombre = input("Ingrese el nombre de la mascota: ")
    mascota.anioNacimiento = int(input("Ingrese el año de nacimiento de la mascota: "))
    mascota.anioadopcion = int(input("Ingrese el año de adopción de la mascota: "))
    mascota.tipo = input("Ingrese el tipo de mascota (perro, gato, etc.): ")
    listamascotas.append(mascota)

for mascota in listamascotas:
    anios_para_adoptar = mascota.anio_cuando_adoptaron()
    print(f"La mascota {mascota.nombre} fue adoptada después de {anios_para_adoptar} años desde su nacimiento.")