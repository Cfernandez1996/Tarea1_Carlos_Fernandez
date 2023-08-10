import sqlite3
conn = sqlite3.connect('rolitas.sqlite')
cur = conn.cursor()

cur.execute('INSERT INTO canciones (titulo, reproducciones) VALUES(?,?)', ('El triste',20))
cur.execute('INSERT INTO canciones (titulo, reproducciones) VALUES(?,?)', ('Almohada',15))
cur.execute('INSERT INTO canciones (titulo, reproducciones) VALUES(?,?)', ('Perfecta',25))

conn.commit() #para forzar la escritura de la base de datos

print('canciones')
cur.execute('SELECT titulo, reproducciones FROM canciones')
for fila in cur:
    print(fila)

cur.execute('SELECT titulo,reproducciones FROM canciones ORDER BY titulo')
#cur.execute('DELETE FROM canciones WHERE titulo = "El triste"') #para borrar un solo elemento de la BD
#cur.execute('DELETE FROM canciones WHERE reproducciones < 100') # para borrar todos los datos de la BD
#la linea 15 lo que hace es borrar todos los datos de la base de datos rolitas
cur.execute('INSERT INTO canciones (titulo ,reproducciones) VALUES ("la loco", 50)')
cur.execute('UPDATE canciones SET reproducciones = 16 WHERE titulo = "Almohada"') # para actualizar algo de la tabla

conn.commit()

cur.close()


