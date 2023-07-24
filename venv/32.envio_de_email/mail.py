import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configurações do servidor SMTP do Office 365
smtp_server = 'smtp.office365.com'
smtp_port = 587
username = 'joaoagrelacampos@hotmail.com'
password = '--'

# Configurações do email
sender = username
receiver = 'joao.campos@consulting.rumos.pt'
subject = 'teste de marcação'
body = 'venho por este meio marcar estes dias'

# Criação do objeto de mensagem
message = MIMEMultipart()
message['From'] = sender
message['To'] = receiver
message['Subject'] = subject

# Adiciona o corpo do email à mensagem
message.attach(MIMEText(body, 'plain'))

# Conexão com o servidor SMTP
server = smtplib.SMTP(smtp_server, smtp_port)
server.starttls()
server.login(username, password)

# Envio do email
server.sendmail(sender, receiver, message.as_string())

# Encerramento da conexão
server.quit()
