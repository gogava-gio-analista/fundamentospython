listanombres = []
while len(listanombres) < 5:
    nombre = len(listanombres) + 1
    nombre_usuario = input(f'Ingrese el nombre {nombre}: ')
    if nombre_usuario.upper() in [n.upper() for n in listanombres]:
        print('El nombre ya está en la lista.')
    else:
        listanombres.append(nombre_usuario)
        print(f'Lista de nombres actualizada: {listanombres}')
print('Lista final de nombres ingresados:', listanombres)