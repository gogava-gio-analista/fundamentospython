import oracledb 

connection = oracledb.connect(user="system", password = 'ORACLE', dsn = 'localhost/FREEPDB1')
print('algo')

sql = "select * from DEPT"

sursor = connection.cursor()

sursor.execute(sql)

row = sursor.fetchone()

print(row)

row = sursor.fetchone()

print(row)

row = sursor.fetchone()

print(row)

row = sursor.fetchone()

print(row)
sursor.close()