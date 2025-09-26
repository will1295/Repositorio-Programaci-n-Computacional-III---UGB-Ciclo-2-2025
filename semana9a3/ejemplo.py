import smtplib
import os
from dotenv import load_dotenv

load_dotenv()

host = os.environ.get("env_host")
puerto = os.environ.get("env_puerto")
usuario = os.environ.get("env_usuario")
password = os.environ.get("env_password")

destinatario = "mwllian@ugb.edu.sv"
asunto = "Prueba"
cuerpo = "Este mensaje se ha mandado con Python"
mensaje = f"Subject: {asunto}\n\n{cuerpo}"

server = smtplib.SMTP(host,puerto)
server.starttls()
server.login(usuario,password)
server.sendmail(usuario,destinatario,mensaje)
server.quit()