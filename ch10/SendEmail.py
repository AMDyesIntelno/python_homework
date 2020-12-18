import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
 
my_sender="a87445214@163.com"
my_pass="YJKVUGOCDHPICKWQ"
my_user="a87445214@163.com"
def mail():
    ret=True
    try:
        msg=MIMEText("Python Email Test","plain","utf-8")
        msg["From"]=formataddr(["Misaka",my_sender])
        msg["To"]=formataddr(["Misaka",my_user])
        msg["Subject"]="Test"
 
        server=smtplib.SMTP_SSL("smtp.163.com")
        server.login(my_sender, my_pass)
        server.sendmail(my_sender,[my_user,],msg.as_string())
        server.quit()
    except Exception:
        ret=False
    return ret

ret=mail()
if ret:
    print("邮件发送成功")
else:
    print("邮件发送失败")