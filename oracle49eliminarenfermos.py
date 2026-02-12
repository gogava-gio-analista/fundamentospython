import oracledb 

class OracleEnfermo:
    def __init__(self):
        self.connection = oracledb.connect(user='system', password='ORACLE', dsn='localhost/FREEPDB1')

    def eliminarEnfermo(self, inscripcion):
        cursor = self.connection.cursor()
        sql = 'delete from enfermo where inscripcion = :param'
        cursor.execute(sql, (inscripcion,))
        registros = cursor.rowcount
        self.connection.commit()
        cursor.close()
        return registros
    
    def selectionar(self):
        cursor = self.connection.cursor()
        sql = 'select inscripcion, apellido from enfermo'
        cursor.execute(sql)
        listaEnfermos = []
        contador = 1
        for row in cursor:
            listaEnfermos.append(row[0])
            print(f'{contador} - {row[1]}')
            contador += 1
        print('seleccione una opcion: ')
        opcion = int(input())
        opcionseleccionado = listaEnfermos[opcion - 1]
        return opcionseleccionado