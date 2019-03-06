import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def SendMail(subs, msgs, senders, passwords, receivers):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    for i in range(0,len(senders)):
        mes = MIMEMultipart()
        mes['From'] = senders[i]
        mes['To'] = receivers[i]
        mes['Subject'] = subs[i]
        mes.attach(MIMEText(msgs[i], 'plain'))
        server.login(senders[i], passwords[i])
        text = mes.as_string()
        server.sendmail(senders[i], receiver[i], text)
    server.quit()

tieu_de = ["Test Gửi mail bằng python 1","Test Gửi mail bằng python 1"]
noi_dung = ["Ahihi không có gì đâu 1","Ahihi không có gì đâu 2"]
sender = ["nghialuffy@gmail.com","nghialuffy@gmail.com"]
pas = ["**********","************"]
receiver = ["nghialuffydell@gmail.com","nghialuffydell@gmail.com"]
SendMail(tieu_de, noi_dung, sender, pas, receiver)