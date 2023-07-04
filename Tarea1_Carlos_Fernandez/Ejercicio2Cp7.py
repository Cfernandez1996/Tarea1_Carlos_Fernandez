"""
Ejercicio 2: Escribe un programa que solicite un nombre de archivo
y después lea ese archivo buscando las líneas que tengan la siguiente
forma:
X-DSPAM-Confidence: 0.8475

"""
contador=0
acumulador_itera=0
nombre=input("Ingrese el nombre del archivo: ")
try:
    nombre1=open(nombre)
except:
    print("El archivo no existe")
    exit()
for linea in nombre1:
    linea=linea.rstrip()
    if not linea.startswith('X-DSPAM-Confidence: '):
        continue
    contador+=1
    x=linea.find(':')
    dire=linea[x+1:]
    promedio=float(dire)
    acumulador_itera+=promedio
    

    #print(dire)

total=acumulador_itera/contador
print("Promedio SPAM confidence: ", total)    
    


