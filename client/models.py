from django.db import models

# Create your models here.
class Client(models.Model):
    class Meta:
        verbose_name_plural='Clients'
    name = models.CharField(max_length=100, verbose_name='Client Name')
    cnpj = models.CharField(max_length=14, unique=True, verbose_name='CNPJ')
    address = models.CharField(max_length=255, verbose_name='Address')
    phone = models.CharField(max_length=15, verbose_name='Phone Number')
    email = models.EmailField(max_length=100, verbose_name='Email')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')


    def __str__(self):
        return f'{self.name} - {self.cnpj}'
    
# class Orders(models.Model):
#     class Meta:
#         verbose_name_plural='Orders'
#     client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='orders', verbose_name='Client')
#     order_number = models.CharField(max_length=20, unique=True, verbose_name='Order Number')
#     order_date = models.DateTimeField(auto_now_add=True, verbose_name='Order Date')
#     status = models.CharField(max_length=20, choices=[('pending', 'Pending'), ('completed', 'Completed')], default='pending', verbose_name='Status')
#     description = models.TextField(verbose_name='Description')
#     total_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name='Total Amount')
#     responsible = models.CharField(max_length=50, verbose_name='Responsible Person', choices=[('Mara Ferreira', 'Mara Ferreira'), ('Aline Zampa', 'Aline Zampa')])

#     def __str__(self):
#         return f'Order {self.order_number} - {self.client.name}'
