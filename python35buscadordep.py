import oracledb
coneccion = oracledb.connect(user='system', password='ORACLE', dsn='localhost/FREEPDB1')

iddepart = input('dime ID del dept')

sql = f'select * from DEPT where DEPT_NO = {iddepart}'
cursor = coneccion.cursor()
cursor.execute(sql)
row = cursor.fetchone()

if row == None:
    print('No existe el departamento')
else:
    nombre = row[1]
    localidad = row[2]
    print(f'{nombre}, {localidad}')

cursor.close()
coneccion.close()
print('fin del mundo') 
