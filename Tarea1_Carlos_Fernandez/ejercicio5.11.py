mayor=0
menor=100

while True:
    try:
        entrada=input("Ingrese un numero o Fin para salir: ")
        if entrada=='Fin' or entrada=='fin':
            break
        numero=float(entrada)    
    except:
        print("ERROR ingrese un numero")
    
    if numero>mayor:
        mayor=numero
    elif numero<menor:
        menor=numero




print("El numero mayor es: ", mayor)
print("el numero nemor es: ", menor)

