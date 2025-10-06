from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib


plantilla = Path(r"C:/Users/johan/Estudios_Serios/curso_hola_mundo/Paquetes_Nativos_python/plantilla.html").read_text("utf-8")
template = Template(plantilla)
cuerpo = template.substitute({"usuario": "Chanchito Feliz, vamossssssssss"})



path = Path(r"C:/Users/johan/Estudios_Serios/curso_hola_mundo/Paquetes_Nativos_python/hola.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "jpardo180@gmail.com"
mensaje["to"] = "jpardo180@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo= MIMEText(cuerpo, "html")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host = "smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() #identificar4nos con el sevidor smtp e identificar el numobre de dominio
    smtp.starttls() #transport layer Security -- encriptacion

    smtp.login("jpardo180@gmail.com","lqbm tgzp lvjb plsf")
    smtp.send_message(mensaje)
    print("correo enviado con exito")