from datetime import datetime, timedelta

#con timedelta puedo agregar o quitar tiempo de una manera mas pragmatica

fecha = datetime(2025,1,1) + timedelta(weeks=1)
fecha2 = datetime(2025,2,1)

delta = fecha2 - fecha

print(delta)
print("dias", delta.days)
print("segundos", delta.seconds)
print("microsegundos", delta.microseconds)
print("total_seconds()", delta.total_seconds())

