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
NUMBER_OF_OBJECTS = 1000

sys.path.append(str(DJANGO_BASE_DIR))
os.environ['DJANGO_SETTINGS_MODULE'] = 'project.settings'
settings.USE_TZ = False

django.setup()

if __name__ == '__main__':
    from faker import Faker
    from client.models import Cliens

    fake = Faker('pt_BR')

    for _ in range(NUMBER_OF_OBJECTS):
        name = fake.name()
        cnpj = fake.cpf()
        address = fake.address()
        phone = fake.phone_number()
        email = fake.email()
        created_at = datetime.now()

        client = Client(
            name=name,
            cnpj=cnpj,
            address=address,
            phone=phone,
            email=email,
            created_at=created_at
        )
        client.save()

    print(f'{NUMBER_OF_OBJECTS} clients created successfully!')
    # Create 1000 orders for each client
  