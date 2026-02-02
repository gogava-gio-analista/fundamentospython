from class32mes import Mes

listameses = []

for i in range(3):
    mes = Mes()
    mes.nombre = input(f'Ingrese el nombre del mes {i + 1}: ')
    mes.temperatura_minima = float(input(f'Ingrese la temperatura mínima de {mes.nombre}: '))
    mes.temperatura_maxima = float(input(f'Ingrese la temperatura máxima de {mes.nombre}: '))
    listameses.append(mes)

print('\nResumen de temperaturas medias por mes:')
for mes in listameses:
    temp_media = mes.calcular_temperatura_media()
    print(f'Mes: {mes.nombre}, temperatura mínima: {mes.temperatura_minima}°C, temperatura máxima: {mes.temperatura_maxima}°C, temperatura media: {temp_media}°C')