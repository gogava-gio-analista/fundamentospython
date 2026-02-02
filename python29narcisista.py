import python28numeronarcicista
final = int(input('dime numero final: '))
for i in range(1, final + 1):
    if python28numeronarcicista.es_narcisista(i):
        print(i)