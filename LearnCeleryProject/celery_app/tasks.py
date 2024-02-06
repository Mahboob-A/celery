from celery import shared_task 
from time import sleep 
from datetime import datetime


@shared_task(name='multiply_task')
def multiple_value(x, y):
    sleep(15)
    return x * y 


@shared_task(name='testing_default_celery_beat')
def print_current_time_by_interval(name):
    print(f'name: {name}')
    print(f'current time is: {datetime.now()}')
    return name 