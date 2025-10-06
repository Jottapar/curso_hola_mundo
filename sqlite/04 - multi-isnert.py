import sqlite3


with sqlite3.connect("curso_hola_mundo/sqlite/app.db") as con:
    cursor = con.cursor()
    usuarios = [
        (5, "Chanchito Feliz"),
        (6, "Otro Chanchito")
    ]
    cursor.executemany(
        "insert into usuarios values(?, ?)",
        usuarios,
    )


