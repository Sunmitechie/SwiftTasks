from django.core.mail import send_mail
from django_q.tasks import async_task

def send_email_notification(subject, message, recipient_list):
    send_mail(
        subject,
        message,
        'your-email@example.com',
        recipient_list,
        fail_silently=False,
     )