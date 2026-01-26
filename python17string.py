print('trabajando con strings en python')
texto = 'hoS primer python YoR44 34 56 ' 
print('uppercase:', texto.upper())  # Convierte todo el texto a mayúsculas
print('lowercase:', texto.lower())  # Convierte todo el texto a minúsculas
print('capitalize:', texto.capitalize())  # Capitaliza la primera letra
print('title:', texto.title())  # Capitaliza la primera letra de cada palabra
print('strip:', texto.strip())  # Elimina espacios en blanco al inicio y final
print('replace:', texto.replace('primer', 'segundo'))  # Reemplaza una subcadena por otra
print('find:', texto.find('Yor'))  # Busca la posición de una subcadena
print('substring [2:7]:', texto[2:7])  # Extrae caracteres del índice 2 al 6
print('length:', len(texto))  # Obtiene la cantidad total de caracteres
print('character at index 4:', texto[4])  # Obtiene el carácter en la posición 4
print('split:', texto.split())  # Divide la cadena en una lista de palabras
print('endswith "56":', texto.endswith('56'))  # Verifica si termina con una cadena específica
print('startswith "hoS":', texto.startswith('hoS'))  # Verifica si comienza con una cadena específica
print('count of "o":', texto.count('o'))  # Cuenta cuántas veces aparece un carácter
print('isalpha for "hoS":', 'hoS'.isalpha())  # Verifica si contiene solo letras
print('isdigit for "34":', '34'.isdigit())  # Verifica si contiene solo dígitos
print('isalnum for "YoR44":', 'YoR44'.isalnum())  # Verifica si contiene letras y dígitos
print('join with "-":', '-'.join(['hoS', 'primer', 'python']))  # Une elementos de una lista con un separador
print('formatting:', 'El texto es: {}'.format(texto))  # Formatea una cadena usando .format()
print(f'formatted string: El texto es: {texto}')  # Formatea una cadena usando f-string
print('splitlines:', 'Linea1\nLinea2\nLinea3'.splitlines())  # Divide la cadena en líneas
print('replace "python" with "Java":', texto.replace('python', 'Java'))  # Reemplaza una palabra por otra
print('count of " ":', texto.count(' '))  # Cuenta los espacios en blanco
print('reverse string:', texto[::-1])  # Invierte el orden de los caracteres
print('isupper for texto:', texto.isupper())  # Verifica si todos los caracteres son mayúsculas
print('islower for texto:', texto.islower())  # Verifica si todos los caracteres son minúsculas
print('swapcase:', texto.swapcase())  # Intercambia mayúsculas por minúsculas y viceversa



