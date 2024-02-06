from celery import shared_task
from django.contrib.auth import get_user_model 
from django.core.mail import send_mail 
from django.conf import settings
from time import sleep
from datetime import datetime 


@shared_task 
def task_send_email(): 
    email_subject = 'Greetings ... from Celery'
    email_body = 'Hello this is a testing email to test celery. If you are reading this email, hope you are sound and well!'
    to_email = ''
    users = get_user_model().objects.all()
    for user in users: 
        to_email = user.email
        send_mail(
            subject=email_subject, 
            message=email_body, 
            from_email=settings.EMAIL_HOST_USER, 
            recipient_list=[to_email], 
            fail_silently=True
        )
    return True 


@shared_task
def task_add_value(x, y):
    print('in add_value task ... sleep mode') 
    sleep(10)
    print('in add_value task ... sleep mode COMPLETED')
    return x + y 


@shared_task
def task_print_current_time_by_interval(name):
    print(f'name: {name}')
    current_time = f'current time is: {datetime.now()}' 
    return current_time 
