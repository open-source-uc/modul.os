from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# TODO: Cambiar a una variable de entorno o un archivo de configuración
SQLALCHEMY_DATABASE_URL ="postgresql://postgres:postgres@localhost:5432/python_db"

# Creamos el motor de la base de datos
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Creamos la sesión de la base de datos
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Creamos la base de datos declarativa
Base = declarative_base()