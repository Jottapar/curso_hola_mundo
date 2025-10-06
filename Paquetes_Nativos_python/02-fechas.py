# import time

# print(time.time())


from datetime import datetime
fecha = datetime(2025,1,1)
fecha2 = datetime(2025,1,1)

ahora = datetime.now()

#dee string a fecha
fechastr = datetime.strptime("2023-01-03", "%Y-%m-%d") #directives

#de fecha a string
print(fecha.strftime("%Y.%m.%d"))

print(
    fecha.year,
    fecha.month,
    fecha.day,
    fecha.hour,
    fecha.minute
)