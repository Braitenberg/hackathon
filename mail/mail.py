import smtplib


class Mail:

    def mail(message):
        email =["y.dian@live.nl", "theaminaloui@hotmail.com", "" ]

        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.ehlo()
            server.starttls()
            server.ehlo()

            server.login('python.novi@gmail.com', 'V=7^GGPh^;gF\,P*')

            subject = 'Feedback'
            body = message

            msg = f"Subject: {subject}\n\n{body}"

            server.sendmail(
                'python.novi@gmail.com',
                email,
                msg.encode("utf8")
            )

            print('test')

        except Exception as e:
            return "Mail versturen is mislukt"

        server.quit()



