import smtplib
import os
from dotenv import load_dotenv 
load_dotenv()
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

HOST = os.getenv("HOST")
PUERTO = os.getenv("PUERTO")
USUARIO = os.getenv("USUARIO")
PASS = os.getenv("PASS")

destinatario = "mwillian@ugb.edu.sv"
asunto = "Prueba de archivo adjunto"
cuerpo = "Enviando archivo adjunto solicitado"

mensaje = MIMEMultipart()
mensaje["From"] = USUARIO
mensaje["To"] = destinatario
mensaje["Subject"] = asunto
mensaje.attach(MIMEText(cuerpo,'plain'))

ruta_archivo = "document.pdf"
nombre_archivo = os.path.basename(ruta_archivo)

with open(nombre_archivo,"rb") as f:
    part = MIMEBase("application","octet-stream")
    part.set_payload(f.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition"
                ,f"attatchment;filename={nombre_archivo}")
mensaje.attach(part)

with smtplib.SMTP(HOST,PUERTO) as server:
    server.starttls()
    server.login(USUARIO,PASS)
    server.sendmail(USUARIO,destinatario
                    ,mensaje.as_string())