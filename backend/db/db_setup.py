from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

load_dotenv()

host = os.getenv("DB_HOST")
port = os.getenv("DB_PORT")
user = os.getenv("DB_USERNAME")
password = os.getenv("DB_PASSWORD")
name = os.getenv("DB_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg2://{user}@{host}:{port}/{name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

def get_db():
    """
    Función para obtener una sesión de la base de datos
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()