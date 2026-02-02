listanumeros = [1, 2, 3, 4, 5]
listapalabras = ["hola", "mundo", "python", "es", "genial", "programar", "en", "lista", "y", "tuplas", "en", "python", 'diversion']
listamixta = [1, "dos", 3.0, True, [5, 6]]

tupla_numeros = (1, 2, 3, 4, 5)
tupla_palabras = ("hola", "mundo", "python")
tupla_mixta = (1, "dos", 3.0, False, (5, 6))

listanumeros.sort(reverse=True)
print(listanumeros)

for i in listapalabras:
    print(i.upper())

for elemento in listamixta:
    print(type(elemento))

for i in listanumeros:
    print(i)

del listapalabras[1:3]
print(listapalabras)