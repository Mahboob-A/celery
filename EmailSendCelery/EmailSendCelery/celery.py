import os 
from celery import Celery 

# settings for celery cli 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'EmailSendCelery.settings')

# create the celery app
app = Celery('EmailSendCelery')

# tell celery to find config from django's settings.py 
app.config_from_object('django.conf:settings', namespace='CELERY')

# to exclude pain of importing all tasks, run autodiscovers_tasks so celery automatically finds all 
# @shared_tasks from tasks.py file 
app.autodiscover_tasks()

