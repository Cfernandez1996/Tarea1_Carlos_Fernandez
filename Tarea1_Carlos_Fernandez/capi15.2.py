import sqlite3
conn = sqlite3.connect('personas.sqlite')
cur = conn.cursor()

#cur.execute('DROP TABLE IF EXISTS chidas')
#cur.execute('CREATE TABLE chidas (nombre TEXT, edad INTERGER, ID TEXT)')
cur.execute('INSERT INTO chidas (nombre, edad, ID) VALUES(?,?,?)', ('Carlos Fernandez', 27, '0801-1996-00332'))
cur.execute('INSERT INTO chidas (nombre, edad, ID) VALUES(?,?,?)', ('Ariana Sarmiento', 18, '0801-2005-00112'))
cur.execute('INSERT INTO chidas (nombre, edad, ID) VALUES(?,?,?)', ('Mercedes Suyapa', 62, '0101-1959-00332'))
cur.execute('INSERT INTO chidas (nombre, edad, ID) VALUES(?,?,?)', ('Luis Ricardo',70, '0801-1957-00000'))

conn.commit()

cur.execute('DELETE FROM chidas WHERE nombre = "Carlos Fernandez"')
#cur.execute('INSERT INTO chidas(nombre, edad, ID) VALUES ("Carlos Betancourt", 27, "0801-1996-10741")')
#cur.execute('DELETE FROM chidas WHERE edad < 100')
conn.commit()


#cur.execute('INSERT INTO canciones (titulo, reproducciones) VALUES(?,?)', ('Perfecta',25))
#cur.execute('DELETE FROM canciones WHERE titulo = "El triste"') #para borrar un solo elemento de la BD
#cur.execute('INSERT INTO canciones (titulo ,reproducciones) VALUES ("la loco", 50)')
##cur.execute('DELETE FROM canciones WHERE reproducciones < 100') # para borrar todos los datos de la BD