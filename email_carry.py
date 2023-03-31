import smtplib
from email.mime.text import MIMEText

def send_mail(message, recipient):
    sender = "isip_m.a.nedvckaiy@mpt.ru"
    password = "lbvedlhcjzqbybmc"
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Сообщение с кодом подтверждения "
        server.sendmail(sender, recipient, msg.as_string())
        return "Сообщение отправлено!"
    except Exception as ex:
        return f"{ex}\nПроверьте ввод данных!"