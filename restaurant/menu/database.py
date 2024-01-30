from sqlalchemy import URL
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import DB_HOST, DB_PORT, DB_USER, DB_PASSWORD, DB_BASE, DB_URL


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


if DB_URL:
    DB = DB_URL.split('@')[1].split(':')[0]
else:
    DB = DB_HOST

url_object = URL.create(
    "postgresql",
    username=DB_USER,
    password=DB_PASSWORD,
    host=DB,
    database=DB_BASE,
    port=DB_PORT,
)


SQLALCHEMY_DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_BASE}"

engine = create_engine(url_object)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
