
def calificaciones(a:float):
    if a>0.90:
        print("Sobresaliente")
    elif a>0.80 and a<90:
        print("notable")
    elif a>0.70 and a<0.80:
        print("Bien")
    elif a>0.60 and a<0.70:
        print("Suficiente")
    elif a>=0.50 and a<0.60:
        print("pasable")
    else:
        print("Reprobado")




contador=int(input("Desea ingresar una nueva nota: 1--> si, 2-->no: "))       

while contador==1:
    
    nota=float(input("Ingrese una nota: "))

    print(calificaciones(nota))
    contador=int(input("Desea ingresar una nueva nota: 1--> si, 2-->no: "))  

    

   




