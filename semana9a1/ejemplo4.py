import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

host = "smtp.gmail.com"
puerto = 587
usuario = "willian120795@gmail.com"
password = "uzrl sgfy iqsq dxgz"
destinatario = "mwillian@ugb.edu.sv"
mensaje = MIMEMultipart()
mensaje["From"] = usuario
mensaje["To"] = destinatario
mensaje["Subject"] = "Mandando archivo adjunto"
cuerpo = "Este es un correo por mime que lleva un archivo adjunto"
texto = MIMEText(cuerpo,'plain')
archivo = "document.pdf"
with open(archivo,"rb") as f:
    part = MIMEBase("application","octet-stream")
    part.set_payload(f.read())
encoders.encode_base64(part)
part.add_header("Content-Disposition",f"attachment;filename={archivo}")
mensaje.attach(part)


server = smtplib.SMTP(host,puerto)
server.starttls()
server.login(usuario,password)
server.sendmail(usuario,destinatario,mensaje.as_string())
server.quit()