from oracle49eliminarenfermos import OracleEnfermo

print('Programa eliminar enfermos')
oracle = OracleEnfermo()
# print('introduzca numero de inscripcion')
dato = oracle.selectionar()
registros = oracle.eliminarEnfermo(dato)
print(f'Enfermos elminados: {registros}')
print('Fin de programa')