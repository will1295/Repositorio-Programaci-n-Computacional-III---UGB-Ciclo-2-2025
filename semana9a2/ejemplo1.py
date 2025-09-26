import smtplib
import os
from dotenv import load_dotenv 
load_dotenv()

HOST = os.getenv("HOST")
PUERTO = os.getenv("PUERTO")
USUARIO = os.getenv("USUARIO")
PASS = os.getenv("PASS")

destinatario = "mwillian@ugb.edu.sv"
asunto = "Prueba"
cuerpo = "Este mensaje se ha mandado por Python"
mensaje = f"Subject: {asunto}\n\n{cuerpo}"

server = smtplib.SMTP(HOST,PUERTO)
server.starttls()
server.login(USUARIO,PASS)
server.sendmail(USUARIO,destinatario,mensaje)
server.quit()