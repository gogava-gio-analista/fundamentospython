numero = int(input("Introduzca un numero: "))

while numero != 1:
    print(numero)
    if numero % 2 == 0:
        numero = numero // 2
    else:
        numero = 3 * numero + 1
print(numero)
print("Fin del programa")