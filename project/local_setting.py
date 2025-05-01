import dj_database_url
import os
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv(encoding='utf-8')

# Agora as variáveis de ambiente do .env estarão disponíveis


# Banco de dados para produção
DATABASES = {
    'default': dj_database_url.config(
        default='postgresql://{user}:{password}@{host}:{port}/{db}?sslmode=require'.format(
            user=os.getenv('DJANGO_DB_USER'),
            password=os.getenv('DJANGO_DB_PASSWORD'),
            host=os.getenv('DJANGO_DB_HOST'),
            port=os.getenv('DJANGO_DB_PORT'),
            db=os.getenv('DJANGO_DB_NAME')
        ),
        conn_max_age=600,
        ssl_require=True
    )
}


# Variáveis de ambiente para produção
SECRET_KEY = os.getenv('DJANGO_SECRET_KEY', 'your-production-secret-key')  # Defina isso no ambiente de produção
DEBUG = os.getenv('DJANGO_DEBUG', 'False') == 'True'

# Se desejar limitar os ALLOWED_HOSTS, altere para um domínio específico
ALLOWED_HOSTS = ['*']  # Em produção, substitua por seu domínio, como 'example.com'
