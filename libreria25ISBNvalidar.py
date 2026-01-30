def validar_ISBN(isbn):
    if len(isbn) != 10:
        return False
    else:
        for i in isbn:
            multiplicar = (isbn.index(i) + 1) * int(i)
            suma = 0
            suma += multiplicar
        if suma % 11 == 0:
            return True
        else:
            return False