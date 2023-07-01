"""palabra=input("Ingresa una palabra: ")

if palabra < 'carlos':
    print("Tu palabra ", palabra, " no es igual")
elif palabra >'carlos':
    print("tu palabra ", palabra, " esta despues de carlos")
else:
    print("ambas tiene la misma letra de inicio")

#el .upper vuelte toda la cadena a mayuscula
cadena=input("ingrese lo que quiera: ")
nueva_cadena=cadena.upper()
print(nueva_cadena)

#el .find busca la posicion de la cadena dentro de la otra pasandole lo que debe de buscar
cadena='carlos dionisio fernandez'
indice=cadena.find('a')
print(indice)

#primero se debe de buscar el caracter para saber desde donde se va a buscar
#despues eso se pasa a una nueva variable(cadena.find('@'))
#cuando ya se tiene la posicion de inicio se debe saber hasta donde se va a buscar cadena.find(' ', nueva)
#por ultimo se toma la porcion de la cadena que se va a cortar cadena[nueva+1:espacio]
cadena='From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008'
nueva=cadena.find('@')
print(nueva)
espacio=cadena.find(' ', nueva)
print(espacio)
direcion=cadena[nueva+1:espacio]
print(direcion)

cadena=' Facebook. Meta Platforms, Inc., Attention: Community Support, 1 Facebook Way, Menlo Park, CA 94025'
nueva=cadena.find(' ')
epacio=cadena.find(':', nueva)
dir=cadena[nueva+1:epacio]
print(dir)"""



