"""
Ejercicio 5: Toma el siguiente código en Python que almacena una cadena:
str = 'X-DSPAM-Confidence:0.8475'
Utiliza find y una parte de la cadena para extraer la porción de la cadena
después del carácter dos puntos y después utiliza la función float para
convertir la cadena extraída en un número de punto flotante.

"""
cad = 'X-DSPAM-Confidence:0.8475'
nueva=cad.find(':')
#espacio=cad.find(' ',nueva)
direccion=cad[nueva+1:]
numero=float(direccion)
print(direccion,numero)
#print(numero)