# =================================================
# VARIABLES EN PYTHON
# =================================================
'''
Una variable es un contenedor que almacena valores.
En Python, las variables se crean al asignarles un valor.
No es necesario declarar el tipo de dato.
'''

# ============ EJEMPLOS DE VARIABLES ============

# 1. Variables de tipo numérico
edad = 25                    # Entero (int)
altura = 1.75               # Decimal (float)
numero_complejo = 3 + 4j    # Número complejo

# 2. Variables de tipo texto
nombre = "Juan"             # Cadena de texto (string)
ciudad = 'Madrid'           # También es válido con comillas simples
mensaje = """Esto es una
cadena multilinea"""        # Múltiples líneas

# 3. Variables booleanas
es_activo = True            # Valor verdadero
es_completado = False       # Valor falso

# 4. Variables de colecciones
lista_numeros = [1, 2, 3, 4, 5]           # Lista (modificable)
tupla_datos = (10, 20, 30)                # Tupla (inmutable)
diccionario = {"nombre": "Ana", "edad": 30}  # Diccionario (clave-valor)
conjunto = {1, 2, 3, 4}                  # Conjunto (único, sin orden)

# ============ OPERACIONES CON VARIABLES ============

# Aritmética
a = 10
b = 3
suma = a + b               # 13
resta = a - b              # 7
multiplicacion = a * b     # 30
division = a / b           # 3.333...
division_entera = a // b   # 3
modulo = a % b             # 1
potencia = a ** b          # 1000

# Concatenación de strings
nombre_completo = "Carlos" + " " + "López"

# ============ VERIFICAR TIPOS ============
# print(type(edad))          # <class 'int'>
# print(type(altura))        # <class 'float'>
# print(type(nombre))        # <class 'str'>
# print(type(es_activo))     # <class 'bool'>

print(f"Variables definidas correctamente. {b}")
print ('el numero es: ', b)
print ('el numero es: ' + nombre)

numero = '6'
texto = 'El numero es: '
numstr = int(numero)
numero 
textstr = int(texto)  # Esto generará un error porque 'El numero es: ' no es un número
print (textstr + numstr)