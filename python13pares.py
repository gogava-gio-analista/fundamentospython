
print('rango de numeros pares')
numero_inicial = 6
numero_final = 20

'''
for numero in range(numero_inicial, numero_final + 1):
    if numero % 2 == 0:
        print("El numero par es: ", numero)
print("Fin del bucle")

'''

while (numero_inicial <= numero_final):
    if numero_inicial % 2 == 0:
        print("El numero par es: ", numero_inicial)
    numero_inicial += 1
print("Fin del bucle")