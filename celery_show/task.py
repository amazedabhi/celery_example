from celery import shared_task
from time import sleep
from django.core.mail import send_mail


@shared_task
def send_mail_task(email, subject, message,):
    send_mail('CELERY YEAH','BEN STOKES',
                'chintz.91@gmail.com',['amazed.abhi15@gmail.com'],
                fail_silently=False)
    send_mail(subject,message,
                'chintz.91@gmail.com',[email],
                fail_silently=False)                
    return None

@shared_task
def sleepy(duration):
    sleep(duration)
    return None