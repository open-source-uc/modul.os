"""
Archivo de EJEMPLO para definir el modelo de usuario
"""

from db.database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
import enum

class Role(enum.Enum):
    user = 1
    admin = 2

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True, nullable=False)
    password = Column(String)
    hashed_password = Column(String)
    # en Relationship uselist=False para que sea 1 a 1. Pero, User puede tener varios perfiles?
    profile = relationship("Profile", back_populates="user", uselist=False)

class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    role = Column(Enum(Role))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="profile")
