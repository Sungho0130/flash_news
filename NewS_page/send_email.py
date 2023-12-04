from celery import shared_task
from django.core.mail import EmailMessage

@shared_task
def send_email_task(message, email):
    email_message = EmailMessage(
        f"새로운 문의 내용",
        f"내용 : {message}\n연락처 : {email}",
        to=['starhochoitest@gmail.com'],
    )
    email_message.send()
