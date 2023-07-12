datos={}
with open('mbox-short.txt') as archivo:
    for j in archivo:
        if j.startswith('From: '):
            posicion=j.index(" ")+1
            contador=j[posicion:].strip()
            datos[contador]=datos.get(contador,0)+1
                    
datos2={}
with open('mbox.txt') as archivo1:
    for i in archivo1:
        if i.startswith('From: '):
            posicion1=i.index(" ")+1
            contador1=i[posicion1:].strip()
            datos2[contador1]=datos2.get(contador1,0)+1

llave = max(datos, key=datos.get) #con esto se obtiene el correo
total = datos[llave] #y con esto se obtiene el valor de los correos 
llave1=max(datos2, key=datos2.get)
tota1=datos2[llave1]

print(llave, ': ', total)
print(llave1,': ',tota1)










