"""
Escribe una función llamada recortar que toma una lista y la modifica, 
removiendo el primer y último elemento, y regresa None. Después escribe una
función llamada medio que toma una lista y regresa una nueva lista que contiene
todo excepto el primero y último elementos
"""
def recortar(cadena):
    cadena.pop(0)
    cadena.pop(-1)
    return None

def medio(cadena):
    return cadena[1:-1]

    
    
n=[1,2,3,4,5,6,7,8]
x=['hola','adios','avion','carro','bici','poo']
otra=medio(x)
recortar(n)
print(n)
print(otra)



    