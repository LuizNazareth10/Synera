# utilizar Faker para gerar dados de clientes falsos baseado no modelo abaixo:
# class Client(models.Model):
#     class Meta:
#         verbose_name_plural:'Clients'
#     name = models.CharField(max_length=100, verbose_name='Client Name')
#     cnpj = models.CharField(max_length=14, unique=True, verbose_name='CNPJ')
#     address = models.CharField(max_length=255, verbose_name='Address')
#     phone = models.CharField(max_length=15, verbose_name='Phone Number')
#     email = models.EmailField(max_length=100, verbose_name='Email')
#     created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created At')


#     def __str__(self):
#         return f'{self.name} - {self.cnpj}'

import os
import sys
from datetime import datetime
from pathlib import Path
from random import choice

import django
from django.conf import settings

DJANGO_BASE_DIR = Path(__file__).parent.parent
NUMBER_OF_OBJECTS = 100

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    from faker import Faker
    from order.models import Order
    from client.models import Client
    
    fake = Faker('pt_BR')
    Order.objects.all().delete()

    for _ in range(NUMBER_OF_OBJECTS):
        # selecionar um cliente aleatório das opções disponíveis
        client = choice(Client.objects.all())
        order_date = datetime.now()
        status = choice(['pending', 'completed'])
        description = fake.text(max_nb_chars=400)
        total_amount = fake.random_number(digits=5, fix_len=True)
        responsible = choice(['Mara Ferreira', 'Aline Zampa'])

        order = Order(
            client=client,
            order_date=order_date,
            status=status,
            description=description,
            total_amount=total_amount,
            responsible=responsible
        )
        order.save()
       

    print(f'{NUMBER_OF_OBJECTS} orders created successfully!')
    # Create 1000 orders for each client
      ## ao rodar esse arquivo eu quero deletar todos os pedidos e criar novos pedidos para cada cliente