listanumeros = []
numero = 0

while numero != -1:
    numero = int(input('Ingrese un número: '))
    if numero != -1:
        listanumeros.append(numero)
    

suma = 0
for n in listanumeros:
    suma += n
print('La suma de los números ingresados es:', suma)

conteo = len(listanumeros)
print('La cantidad de números ingresados es:', conteo)

numeros_pares = [n for n in listanumeros if n % 2 == 0]
print('Números pares ingresados:', numeros_pares)

numeros_impares = [n for n in listanumeros if n % 2 != 0]
print('Números impares ingresados:', numeros_impares)

numeros_impares_sum = 0
for n in numeros_impares:
    numeros_impares_sum += n
print('La suma de los números impares es:', numeros_impares_sum)

numeros_pares_sum = 0
for n in numeros_pares:
    numeros_pares_sum += n
print('La suma de los números pares es:', numeros_pares_sum)