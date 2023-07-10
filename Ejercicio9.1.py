"""
Escribe un programa que lee las palabras en words.txt y las almacena
como claves en un diccionario. No importa qué valores tenga. Luego
puedes utilizar el operador in como una forma rápida de revisar si una
cadena está en el diccionario.
"""
diccionario=dict()

with open('words.txt','r') as archivo:
    for i in archivo:
        palabra=i.split()
        for j in palabra:
            if j not in diccionario:
                diccionario[j]=1
        
#print(diccionario)
cadena=input('Ingrese la cadena que desea buscar: ')
if cadena in diccionario:
    print("la cadena si existe")
else:
    print("la cadena que ingreso no existe")






