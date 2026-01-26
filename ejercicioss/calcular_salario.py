# Entrada de datos
horas = int(input("INTRODUZCA HORAS SEMANALES: "))
importe_hora = float(input("INTRODUZCA IMPORTE HORA: "))
kilometros = int(input("INTRODUZCA KILOMETROS: "))

# Cálculo de horas extra
if horas > 36:
    horas_extra = horas - 36
    horas_normales = 36
else:
    horas_extra = 0
    horas_normales = horas

# Salarios
salario_base = horas_normales * importe_hora
salario_horas_extra = horas_extra * (importe_hora + 1.5)
salario_bruto = salario_base + salario_horas_extra

# Destino
if kilometros < 101:
    destino = "PROVINCIAL"
elif kilometros <= 900:
    destino = "NACIONAL"
else:
    destino = "INTERNACIONAL"

# Retención
if salario_bruto <= 250:
    retencion = 0
elif salario_bruto <= 500:
    retencion = 0.20
else:
    retencion = 0.50

# IVA
iva = salario_bruto * 0.16
salario_neto = salario_bruto - iva

# Salida
print("\n---------------------------------------------------")
print(f"HORAS TRABAJADAS:           {horas}")
print(f"HORAS EXTRAS:               {horas_extra}")
print(f"IMPORTE DE LA HORA:         {importe_hora}")
print(f"DISTANCIA EN KM:            {kilometros}")
print(f"DESTINO:                    {destino}")
print(f"RETENCION:                  {int(retencion * 100)}%")
print(f"SALARIO BASE:               {salario_base:.2f}")
print(f"SALARIO HORAS EXTRA:        {salario_horas_extra:.2f}")
print(f"SALARIO BRUTO:              {salario_bruto:.2f}")
print(f"IVA (16%):                  {iva:.2f}")
print("---------------------------------------------------")
print(f"SALARIO TOTAL:              {salario_neto:.2f}")
print("---------------------------------------------------")
print("FIN DE PROGRAMA")
