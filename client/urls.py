from django.urls import path
from client import views

app_name = 'client'

urlpatterns = [
    path('', views.index,name='index'),
    path('client/<int:client_id>/', views.client_detail, name='client_detail'),
    path('client/create/', views.client_create, name='client_create'),
]