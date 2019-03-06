import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
mes = MIMEMultipart()
sender = r"nghialuffy@gmail.com"
receiver = r"nghialuffydell@gmail.com"
mes['From'] = sender
mes['To'] = receiver
mes['Subject'] = "Tiêu đề của gmail"
msg = "Nội dung của mail"
mes.attach(MIMEText(msg,'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(sender, "*************")
text = mes.as_string()
server.sendmail(sender,receiver,text)
server.quit()