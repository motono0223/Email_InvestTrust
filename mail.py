# https://qiita.com/kawa-Kotaro/items/460977f050bf0e2828f2
import smtplib
from email.mime.text import MIMEText
from email.utils import formatdate

MAIL_ADDRESS = "xxxxxxxx@gmail.com"
PASSWORD = "password"

def send_mail(to_addr, subject, message):
    smtpobj = smtplib.SMTP('smtp.gmail.com', 587)
    smtpobj.ehlo()
    smtpobj.starttls()
    smtpobj.ehlo()
    print("Login: ", smtpobj.login(MAIL_ADDRESS, PASSWORD))
    print("--------------------------------------")

    msg = MIMEText(message)
    msg['Subject'] = subject
    msg['From'] = MAIL_ADDRESS
    msg['To'] = to_addr
    msg['Date'] = formatdate()

    smtpobj.sendmail(MAIL_ADDRESS, to_addr, msg.as_string())
    smtpobj.close()
    print("Done")
    print("--------------------------------------")

