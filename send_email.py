import smtplib
import ssl


def send_mail(subject, body):
    host = "smtp.gmail.com"
    port = 465

    username = "avkr258@gmail.com"
    password = "jqcr avhr hhxo gmdu"

    receiver = "avkr258@gmail.com"
    context = ssl.create_default_context()

    subject = subject.encode("utf-8")
    body = body.encode("utf-8")

    message = f"Subject: {subject.decode('utf-8')}\n\n{body.decode('utf-8')}"

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message.encode('utf-8'))
