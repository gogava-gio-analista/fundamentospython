from oracledbConection import consulta

hospcod = int(input('Dime id de hospital: '))
nombre = input('Nombre de hospital: ')
direccion = input('Dirección: ')
telefono = input('Teléfono: ')
numcama = int(input('Numero de camas: '))

sql = f"insert into hospital values({hospcod}, '{nombre}', '{direccion}', '{telefono}', {numcama})"

consulta(sql)