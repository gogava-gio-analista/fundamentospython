from oracledbConection import cursor

apellido = input('introduce apellido: ')
funcion = input('introduce su funcion: ')
turno = input('introduce su turno: ')
salario = input('introduce su salario: ')
salaCodigo = input('introduce su codigo de sala: ')

sql = 'select dsitinct hospital_cod, nombre from hospital'
cursor.execute(sql)


