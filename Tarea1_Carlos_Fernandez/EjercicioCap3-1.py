horas=int(input("Ingrese la horas trabajadas: "))
tarifa=float(input("Ingrese la tarifa por hora: "))

if horas>40:
    horas_extras=horas-40
    salario=(horas*tarifa)+(horas_extras*(tarifa*1.5))
    print("su sueldo es de: ",salario)
else:
    total=horas*tarifa
    print("Su salario es de: ", total)