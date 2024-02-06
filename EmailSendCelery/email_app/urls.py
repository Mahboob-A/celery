from django.urls import path 

from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('send-email/', views.send_email_all_users, name='send_email_all_users'), 
    path('task-result/<str:task_id>/', views.task_result, name='task_result'), 
]