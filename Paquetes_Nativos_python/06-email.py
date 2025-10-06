from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib


#"C:\Users\johan\Estudios_Serios\curso_hola_mundo\Paquetes_Nativos_python\hola.png"

path = Path(r"C:/Users/johan/Estudios_Serios/curso_hola_mundo/Paquetes_Nativos_python/hola.png")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje["from"] = "jpardo180@gmail.com"
mensaje["to"] = "jpardo180@gmail.com"
mensaje["subject"] = "Esta es una prueba"
cuerpo= MIMEText("Cuerpo del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host = "smtp.gmail.com", port=587) as smtp:
    smtp.ehlo() #identificar4nos con el sevidor smtp e identificar el numobre de dominio
    smtp.starttls() #transport layer Security -- encriptacion

    smtp.login("jpardo180@gmail.com","lqbm tgzp lvjb plsf")
    smtp.send_message(mensaje)
    print("correo enviado con exito")