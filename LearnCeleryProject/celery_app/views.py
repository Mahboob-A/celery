from django.shortcuts import render

from LearnCeleryProject.celery import add_value
from celery_app.tasks import multiple_value 
from celery.result import AsyncResult

# testing celery 
'''
def home(request): 
    print('home...')
    result = add_value.apply_async(args=[25, 250])
    print("sum: ", result)
    result2 = multiple_value.delay(10, 20)
    print('multiple: ', result2)
    return render(request, 'celery_app/home.html')
'''

def home(request): 
    print('home...')
    result = add_value.apply_async(args=[25, 250])
    print("sum: ", result)

    # Async Object Methods 
    print()
    print('Task Ready: ', result.ready())
    print('Task Successful: ', result.successful())
    print('Task Failed: ', result.failed())
    return render(request, 'celery_app/home.html', {'result' : result})

def task_result(request, task_id): 
    result = AsyncResult(task_id)
    # Async Object Attributes | .id, task_id, .state, .status, .result 
    # result.state 

    # Async Object Methods 
    print('\n')
    print('Task Ready: ', result.ready())
    print('Task Successful: ', result.successful())
    print('Task Failed: ', result.failed())

    # get() provides the value of the task 
    # get is like synchronous execution. unless and until the task is completed, the process will be blocked 
    # using get. so, only use get() only when the successfull() returns True. 
    # print('Get Task Info: ', result.get()) not like this. 
    if result.successful(): 
        print('Task Value is: ', result.get())
    
    return render(request, 'celery_app/task_result.html', {'result' : result}) 

def about(request):
    return render(request, 'celery_app/about.html')

def contact(request): 
    return render(request, 'celery_app/contact.html') 

