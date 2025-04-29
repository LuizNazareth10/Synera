from django.db import models
from client.models import Client

# Create your models here.
class Order(models.Model):
    class Meta:
        verbose_name_plural='Orders'
        verbose_name='Order'
    name = models.CharField(max_length=50, verbose_name='Name')
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders', verbose_name='Client')
    # order_number = models.CharField(max_length=20, unique=True, verbose_name='Order Number')
    order_date = models.DateTimeField(auto_now_add=True, verbose_name='Order Date')
    status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', verbose_name='Status')
    description = models.TextField(verbose_name='Description')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total Amount')
    responsible = models.CharField(max_length=50, verbose_name='Responsible Person', choices=[('Mara Ferreira', 'Mara Ferreira'), ('Aline Zampa', 'Aline Zampa')])

    def __str__(self):
        return f'Order {self.name} - {self.client.name}'
