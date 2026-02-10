from oracledbConection import consulta

# id = int(input('Dime id de departamento: '))
# nombre = input('nombre de departamento: ')
# localidad = input('localidad: ')

# sql = f"insert into DEPT values({id}, '{nombre}', '{localidad}')"

# consulta(sql)

sql = 'select * from emp'

consulta(sql)