import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

host = "smtp.gmail.com"
puerto = 587
usuario = "willian120795@gmail.com"
password = "uzrl sgfy iqsq dxgz"
destinatario = "mwillian@ugb.edu.sv"
mensaje = MIMEMultipart('alternative')
mensaje["From"] = usuario
mensaje["To"] = destinatario
mensaje["Subject"] = "Probando el uso de MIME"
cuerpo = "Este es un correo por mime"
texto = MIMEText(cuerpo,'plain')
mensaje.attach(texto)
html = "" \
"<html>" \
"<body>" \
"<h1> Hola! </h1>" \
"<p> Este correo se puede dinamizar por medio del html</p>" \
"<img src='https://ugb.edu.sv/wp-content/uploads/2023/06/UGB_LOGOTIPO_HORIZONTAL.png'></img>"
"</body>"
"</html>"
""
texto_html = MIMEText(html,'html')
mensaje.attach(texto_html)

server = smtplib.SMTP(host,puerto)
server.starttls()
server.login(usuario,password)
server.sendmail(usuario,destinatario,mensaje.as_string())
server.quit()