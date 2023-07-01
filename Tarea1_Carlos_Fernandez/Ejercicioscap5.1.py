#amigo=['Carlos', 'Ariana', 'Chacon', 'Daniel', 'Maria']

#for amigos in amigo:
 #   print("Buenos dias amigo: ", amigos)

#print("Fin del bucle for")    

#contador=0
#total=0
#for valor in [10,2,17,9,78]:
  #  contador=contador+1
   # total=total+valor

#print("la cantidad de elementos es: ", contador)
#print("El total de la suma es: ", total)

mayor=None
print("valor inicial: ", mayor)
for valor in [3, 41, 12, 9, 74, 15]:
    if mayor is None or valor > mayor :
        mayor=valor
        print("Bucle: ", valor, mayor)

print("Fin del bucle: ",mayor)  




