contador = 0
suma = 0
numero = -1

while numero != 0:
    numero = int(input("Introduzca un numero (0 para terminar): "))
    suma += numero
    contador += 1
print('numeros introducidos:', contador)  
print("La suma de los numeros introducidos es: ", suma)