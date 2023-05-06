from dotenv import load_dotenv
import os

load_dotenv('infra/.env')

POSTGRES_USER = os.environ.get('DB_HOST')
POSTGRES_PASSWORD = os.environ.get('DB_PORT')
DB_NAME = os.environ.get('DB_NAME')
DB_PORT = os.environ.get('DB_PORT')
DB_HOST = os.environ.get('DB_HOST')
