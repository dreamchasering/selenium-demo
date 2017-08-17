#发送HTML格式的邮件
import smtplib
from email.mime.text import MIMEText
from email.header import Header

#发送邮箱服务器
smtpserver='smtp.163.com'
#发送邮箱用户/密码
user='username@163.com'
password='123456'
#发送邮箱
sender='username@163.com'
#接受邮箱
receiver='receive@163.com'
#发送邮箱主题
subject='python email test'

#编写HTML类型的邮件正文
msg=MIMEText('<html><h1>你好！</h1></html>','html','utf-8')
msg['Subject']=Header(subject,'utf-8')

#连接发送邮件
smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msg.as_string())
smtp.quit()