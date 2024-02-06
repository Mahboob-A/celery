from django.urls import path 
from .views import home, about, contact, task_result

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('task_result/<str:task_id>/', task_result, name='task_result')
]
