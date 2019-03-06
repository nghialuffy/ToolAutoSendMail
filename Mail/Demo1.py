import smtplib
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(r"nghialuffy@gmail.com",r"*************")
msg = "Nội dung cần gửi".encode(encoding="utf-8",errors="strict")
server.sendmail(r"nghialuffy@gmail.com",r"nghialuffydell@gmail.com", msg)
server.quit()