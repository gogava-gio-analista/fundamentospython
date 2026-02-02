provincias = dict(
    {
        'Buenos Aires': 'BA',
        'Córdoba': 'CBA',
        'Santa Fe': 'SF',
        'Mendoza': 'MZA',
        'Tucumán': 'TUC',
    }
)

print(provincias)

for clave, valor in provincias.items():
    print(f'La provincia de {clave} tiene como abreviatura {valor}')

    
provincias.setdefault('Salta', 'SAL')