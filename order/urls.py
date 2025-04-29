from django.urls import path
from order import views

app_name = 'order'

urlpatterns = [
    path('', views.index, name='index'),
    path('order/order_create/', views.order_create, name='order_create'),
    path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    # path('order/<int:order_id>/', views.order_detail, name='order_detail'),
    # path('order/create/', views.order_create, name='order_create'),
]
