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

# finput = open(r"E:\WordSpace\Visual Studio Code\Python\loccmtgmail\input.txt",'r',encoding='utf-8')
# sinput = finput.read()
sinput = input("Nhập code HTML vào đây: ")

c0ut=0
lisres=[]
res=""
for i in range(0,len(sinput)):
    if(sinput[i]==r"@"):
        c0ut+=1
        j=i
        k=i
        while(sinput[j]!=r">"):
            if(sinput[j]==" "):
                break
            j-=1
        while(sinput[k]!=r"<"):
            if(sinput[k]==" "):
                break
            k+=1
        for x in range(j+1,k):
            res+=sinput[x]
        lisres.append(res)
        res=""
#finput.close()
print("--------DANH SACH GMAIL--------")
for i in lisres:
    print(i)
print("Có tổng cộng {0} gmail".format(c0ut))

print("-------------------------------")

tieu_de = input("Tiêu đề của gmail: ")
noi_dung =input("Nội dung của gmail: ")
sender = input("Tên tài khoản: ")
pas = input("Mật khẩu: ")
c0ut=0
for i in lisres:
    SendMail(tieu_de, noi_dung, sender, pas, i)
    c0ut+=1

print("------------Done------------")
print("Bạn đã gửi được {0} gmail đi".format(c0ut))
print("----PRESS ANY KEY TO EXIT---")
i=input()
