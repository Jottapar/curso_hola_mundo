#numeros aleatorios

import random
import string #modulo de python que contiene a-z A-Z 0-9

lista= [1,2,3,4,5,6,7,8]
lista2= [1,2,3,4,5,6,7,8]

random.shuffle(lista)

print(
    random.random(), #numero aleatorio entre 0 y 1
    random.randint(1,10), #generar num aletorio entre un numero y otro
    lista, #desordenar numeros
    random.choice(lista2), #un elemnto aleatorio de una lista
    random.choices(lista2,k=3), #n elementos aleatoria de una lista
    random.choices("abscdefghi.,123",k=3), #longitud de caracteres a mostrar
)

chars = string.ascii_letters
digitos = string.digits

seleccion = random.choices(chars+digitos, k=16)

print(seleccion)

password = "".join(seleccion)

print(password)