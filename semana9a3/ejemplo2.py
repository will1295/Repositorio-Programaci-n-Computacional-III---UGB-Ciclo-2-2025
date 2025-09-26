import smtplib
import os
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

load_dotenv()

host = os.environ.get("env_host")
puerto = os.environ.get("env_puerto")
usuario = os.environ.get("env_usuario")
password = os.environ.get("env_password")

destinatario = "mwllian@ugb.edu.sv"
asunto = "Prueba"
cuerpo = "Este mensaje se ha mandado con Python"

mensaje = MIMEMultipart()
mensaje["From"] = usuario
mensaje["To"] = destinatario
mensaje["Subject"] = asunto
mensaje.attach(MIMEText("Mandando archivo adjunto","plain"))

archivo = "document.pdf"
with open(archivo,"rb") as f:
    part = MIMEBase("application","octet-stream")
    part.set_payload(f.read())

encoders.encode_base64(part)
part.add_header("Content-Disposition"
                ,f"attatchment;filename={archivo}")
mensaje.attach(part)

with smtplib.SMTP(host,puerto) as server:
    server.starttls()
    server.login(usuario,password)
    server.sendmail(usuario,destinatario
                    ,mensaje.as_string())

