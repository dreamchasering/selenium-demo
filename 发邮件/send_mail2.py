#发送带附件的邮件
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

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

#发送的附件
sendfile=open('D:\\python\\report\\log.txt','rb').read()

att=MIMEText(sendfile,'base64','utf-8')
att["Content-Type"]='application/octet-stream'
att["Content-Disposition"]='attachment;filename="log.txt"'

msgRoot=MIMEMultipart('related')
msgRoot['Subject']=subject
msgRoot.attach(att)

#连接发送邮件
smtp=smtplib.SMTP()
smtp.connect(smtpserver)
smtp.login(user,password)
smtp.sendmail(sender,receiver,msgRoot.as_string())
smtp.quit()