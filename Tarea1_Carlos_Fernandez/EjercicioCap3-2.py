

try:
    horas=int(input("Ingrese las horas trabajadas: "))
    tarifa=float(input("Ingrese la tarifa por hora: "))
    if horas>40:
        horas_extras=horas-40
        horas_trabajadas=40
        
        salario=(horas_trabajadas*tarifa)+((horas_extras*tarifa)*1.5)
        print("Su sueldo es de: ", salario)

    else:
        total=horas*tarifa
        print("Su sueldo es de: ", total) 
            
except:
    print("ERROR, Por favor introduzca un numero")