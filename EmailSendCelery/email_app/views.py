
from django.shortcuts import render
from django.http import HttpResponse 
from .tasks import task_add_value, task_send_email
from celery.result import AsyncResult

def home(request): 
    return render(request, 'email_app/home.html')


def send_email_all_users(request): 
    result = task_send_email.delay()
    print('task is: ', result)
    return render(request, 'email_app/task_home.html', {'result' : result})


def task_result(request, task_id): 
    result = AsyncResult(task_id)
    return render(request, 'email_app/task_result.html', {'result' : result})












