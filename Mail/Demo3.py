import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


def SendMail(sub, msg, sender, password, receiver):
    mes = MIMEMultipart()
    mes['From'] = sender
    mes['To'] = receiver
    mes['Subject'] = sub
    mes.attach(MIMEText(msg, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender, password)
    text = mes.as_string()
    server.sendmail(sender, receiver, text)
    server.quit()

tieu_de = "Test Gửi mail bằng python"
noi_dung = "Ahihi không có gì đâu"
sender = "nghialuffy@gmail.com"
pas = "************"
receiver = "nghialuffydell@gmail.com"
SendMail(tieu_de, noi_dung, sender, pas, receiver)
