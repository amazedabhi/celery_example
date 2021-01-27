from django.core.mail import send_mail


def send_mail_without_celery():
    send_mail('CELERY WORKED YEAH','hello',
                'chintz.91@gmail.com',['srpvtltdngp@gmail.com'],
                fail_silently=False)
    return None
