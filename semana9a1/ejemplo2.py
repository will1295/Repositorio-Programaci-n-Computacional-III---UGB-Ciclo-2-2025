import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
puerto = 587
usuario = "willian120795@gmail.com"
password = "uzrl sgfy iqsq dxgz"
destinatario = "mwillian@ugb.edu.sv"
mensaje = MIMEMultipart()
mensaje["From"] = usuario
mensaje["To"] = destinatario
mensaje["Subject"] = "Probando el uso de MIME"
cuerpo = "Este es un correo por mime"
texto = MIMEText(cuerpo,'plain')
mensaje.attach(texto)

server = smtplib.SMTP(host,puerto)
server.starttls()
server.login(usuario,password)
server.sendmail(usuario,destinatario,mensaje.as_string())
server.quit()