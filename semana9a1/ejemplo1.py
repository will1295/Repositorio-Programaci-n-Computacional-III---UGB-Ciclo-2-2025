import smtplib

host = "smtp.gmail.com"
puerto = 587
usuario = "willian120795@gmail.com"
password = "uzrl sgfy iqsq dxgz"

destinatario = "mwillian@ugb.edu.sv"
asunto = "Prueba"
cuerpo = "Este es un correo generado desde Python"
mensaje = f"Subject: {asunto} \n\n{cuerpo}"

server = smtplib.SMTP(host,puerto)
server.starttls()
server.login(usuario,password)
server.sendmail(usuario,destinatario,mensaje)
server.quit()