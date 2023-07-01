total=0
cantidad_numeros=0
while True:
    try:
        entrada=input("Ingrese un NUMERO o fin para salir: ")
        if entrada=='Fin' or entrada=='fin':
            break

        numero=float(entrada)
        total+=numero
        cantidad_numeros+=1

    except:
        print("ERROR ingrese un numero")


media=total/cantidad_numeros
print(total, cantidad_numeros, media)                       


