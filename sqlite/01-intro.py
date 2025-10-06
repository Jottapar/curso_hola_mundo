import sqlite3

#Conectarse a la base de datos
con = sqlite3.connect("curso_hola_mundo/sqlite/app.db")


#Para poder realizar consultas a nuestra base de datos (Crear consultas)
#intermediario entre sqlite y el programador
cursor = con.cursor()

#para poder ejecutar consultas lo hare con el metodo de execute
cursor.execute(
    """
    CREATE TABLE  if not exists usuarios
    (id integer primary key, nombre VARCHAR(50))
    """
)

#para Olbilar que se ejecute la consulta, y comprometer los cambios
con.commit()



con.close()


