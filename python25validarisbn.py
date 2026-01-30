from libreria25ISBNvalidar import validar_ISBN
isbn = input("Ingrese el ISBN a validar: ")
resultado = validar_ISBN(isbn)
print("El ISBN es válido:", resultado)