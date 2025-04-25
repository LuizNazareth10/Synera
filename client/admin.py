from django.contrib import admin

# Register your models here.
from client.models import Client, Orders

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'cnpj', 'address', 'phone', 'email', 'created_at')
    search_fields = ('name', 'cnpj')
    list_filter = ('created_at',)
    ordering = ('-created_at',)

@admin.register(Orders)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('client', 'order_number', 'order_date', 'status', 'description', 'total_amount', 'responsible')
    search_fields = ('order_number', 'client__name')
    list_filter = ('status', 'order_date')
    ordering = ('-order_date',)