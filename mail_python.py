import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_ssl_host="smtp.gmail.com"
smtp_ssl_port=int(587) #465
USERNAME="jamescyber0072@gmail.com"
PASSWORD="zroazokxdljdwwvb"  #this is the password which i have generated for this python app. its not the gmail password of this account.
sender=USERNAME
targets="rootuser2183@gmail.com" #for multiple use ["abc@xyz.com","ab@xy.com"]

text="Site is not working properly"
msg=MIMEMultipart()
msg["Subject"]="!!Error!!"
msg["from"]=sender
msg["to"]=targets
msg.attach(MIMEText(text))

server=smtplib.SMTP(smtp_ssl_host,smtp_ssl_port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(USERNAME,PASSWORD)
server.sendmail(sender,targets,msg.as_string())

server.quit()

#(535, b'5.7.8 Username and Password not accepted. Learn more at\n5.7.8  https://support.google.com/mail/?p=BadCredentials k12sm11635648pfp.158 - gsmtp')
