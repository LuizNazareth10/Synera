from django.contrib import admin
from .models import Order
# Register your models here.

@admin.register(Order)
class OrdersAdmin(admin.ModelAdmin):
    list_display = ('name','client', 'order_date', 'status', 'description', 'total_amount', 'responsible')
    search_fields = ('client__name',)
    list_filter = ('status', 'order_date')
    ordering = ('-order_date',)