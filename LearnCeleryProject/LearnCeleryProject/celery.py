import os
from celery import Celery
from time import sleep 
from datetime import datetime

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LearnCeleryProject.settings')

app = Celery('LearnCeleryProject')

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(['celery_app.tasks', ])

# if we want to create task in seperate tasks.py then use: from celery import shared_task decorator
@app.task 
def add_value(x, y): 
    sleep(10)
    return x + y 


@app.task(name='testing_default_celery_beat1')
def print_current_time_by_interval_1(name):
    print('name: ', name)
    print('current time is: ', datetime.now())
    return name 




# another way of config default celery beat 
app.conf.beat_schedule = {
    'print_current_time_by_interval-1' : {
        'task' : 'celery_app.tasks.print_current_time_by_interval', 
        'schedule' : 10, # in secconds 
        'args' : ('Mahboob Alam',) 
    }
}

@app.task(bind=True, ignore_result=True)
def debug_task(self):
    print(f'Request: {self.request!r}')