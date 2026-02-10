import oracledb 

connection = oracledb.connect(user="system", password = 'ORACLE', dsn = 'localhost/FREEPDB1')
print('algo')

sql = "select * from DEPT"

cursor = connection.cursor()

cursor.execute(sql)

row = cursor.fetchone()

for numero, nombre, localidad in cursor:
    print(nombre)
