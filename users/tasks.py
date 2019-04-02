from celery import shared_task
from django.core.mail import send_mail

from BookCenter import settings


@shared_task
def send_active_email(token, username, email):
    subject = "激活邮件"
    message = ""
    sender = settings.EMAIL_FROM
    receiver = [email]
    html_message = '<a href="http://127.0.0.1:8000/user/active/%s/">http://127.0.0.1:8000/user/active/</a>' % token
    send_mail(subject, message, sender, receiver, html_message=html_message)
