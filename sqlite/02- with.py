import sqlite3

#With para a llamar al metodo __exit__ de la clase y automaticamente cuando termine ejecuta el cloese(), pero si antes de cerrar
#no hay ningun error entonces ejecuta el commit()
with sqlite3.connect("curso_hola_mundo/sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE  if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50))
        """
    )

