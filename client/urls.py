from django.urls import path
from client import views

app_name = 'client'

urlpatterns = [
    path('', views.index,name='index')
]
