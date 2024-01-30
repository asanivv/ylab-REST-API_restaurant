import os

from dotenv import load_dotenv

load_dotenv()

DB_URL = os.environ.get('DATABASE_URL')
DB_HOST = os.environ.get('DB_HOST')
DB_PORT = os.environ.get("DB_PORT")
DB_USER = os.environ.get("DB_USERNAME")
DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_BASE = os.environ.get("DATABASE")
