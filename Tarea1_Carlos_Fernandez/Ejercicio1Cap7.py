"""
Ejercicio 1: Escribe un programa que lea un archivo e imprima su contenido (línea por línea),
todo en mayúsculas. Al ejecutar el programa,
debería parecerse a esto:
python shout.py
Ingresa un nombre de archivo: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
RETURN-PATH: <POSTMASTER@COLLAB.SAKAIPROJECT.ORG>
RECEIVED: FROM MURDER (MAIL.UMICH.EDU [141.211.14.90])
BY FRANKENSTEIN.MAIL.UMICH.EDU (CYRUS V2.3.8) WITH LMTPA;
SAT, 05 JAN 2008 09:14:16 -0500
"""
nombre_archivo=input("Ingrese el nomnre del archivo que desea abrir")
try:
    n=open(nombre_archivo)
except:
    print("El archivo no existe")
    exit()
for indice in n:
    indice=indice.rstrip()
    print(indice.upper())
    