from libreria24validaciondni import validardni

dni = int(input("Introduce tu DNI sin letra: "))
letra = validardni(dni)
dniconletra = str(dni) + letra
print("Tu DNI completo es: " + dniconletra)
output = input("El DNI " + dniconletra + " es correcto? (si/no): ")
if output.lower() == "si":
    print("DNI validado correctamente.")
else:
    print("DNI incorrecto. Por favor, verifica los datos.")