from django.core.mail import EmailMultiAlternatives


import threading


class EmailThread(threading.Thread):

    def __init__(self, email):
        self.email = email
        threading.Thread.__init__(self)

    def run(self):
        self.email.send(fail_silently=False)


class Util:
    @staticmethod
    def send_email(email_subject, sender, receiver, html_content):
        email = EmailMultiAlternatives(
            subject=email_subject, from_email=sender, to=[receiver])
        email.attach_alternative(html_content, "text/html")
        EmailThread(email).start()


