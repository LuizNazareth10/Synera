# Synera

Passo a passo:

django-admin startproject project .

python manage.py startapp app

colocar app nos settings

criar base_templates/global/base.html, static/global/style.css

criar views/__init__.py (adicionar as views la) e os arquivos de views necessarios

criar os models e conectar na base de dados

criar um index na view, adicionar na urls do app e dps include na urls do project

Criar superUser (createsuperuser)

adicionar a classes do app dentro do admin para que la apareça.

configurar o base.html e o style.css