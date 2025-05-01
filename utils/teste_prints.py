import psycopg2
from dotenv import load_dotenv
import os

load_dotenv()

conn = psycopg2.connect(
    dbname=os.getenv("DJANGO_DB_NAME"),
    user=os.getenv("DJANGO_DB_USER"),
    password=os.getenv("DJANGO_DB_PASSWORD"),
    host=os.getenv("DJANGO_DB_HOST"),
    port=os.getenv("DJANGO_DB_PORT")
)

print("Conexão bem-sucedida!")
conn.close()
