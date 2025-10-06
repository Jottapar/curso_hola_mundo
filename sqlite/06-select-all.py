import sqlite3


with sqlite3.connect("curso_hola_mundo/sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("select * from Usuarios")
    print(cursor.fetchall())