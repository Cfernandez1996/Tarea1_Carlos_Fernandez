try:
    nota=float(input("Ingrese su calificacion: "))

    if nota>=0.9:
               input("Sobresaliente")
    elif nota==0.8:
            print("Satifactorio")
    elif nota==0.7:
              print("Muy bueno")
    elif nota==0.6:
                print("suficiente")
    elif nota<=0.6:
             print("REPROBADO")
             
    

except:
    print("ingrese un numero")
