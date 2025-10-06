import sqlite3


with sqlite3.connect("curso_hola_mundo/sqlite/app.db") as con:
    cursor = con.cursor()

    #el segundo argumento debe ser una tupla
    cursor.execute(
        #la consulta como primer argumento y los valores como una tupla es para evitar un SQLInyectio
        "insert into usuarios values(?, ?)",
        (2, "Hola mundo"),
    )


