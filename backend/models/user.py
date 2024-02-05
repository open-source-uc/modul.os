"""
Archivo de EJEMPLO para definir el modelo de usuario
"""

from .database import Base
from sqlalchemy import Column, Integer, String, ForeignKey, Enum
from sqlalchemy.orm import relationship
from sqlalchemy_utils import PasswordType, EmailType
import enum

class Role(enum.Enum):
    user = 1
    admin = 2

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(EmailType, unique=True, index=True, nullable=False)
    password = Column(PasswordType(
        schemes=[
            'pbkdf2_sha512',
            'md5_crypt'
        ],
        deprecated=['md5_crypt']
        ), nullable=False
    )
    # en Relationship uselist=False para que sea 1 a 1. Pero, User puede tener varios perfiles?
    profile = relationship("Profile", back_populates="user", uselist=False)
    day_schedules = relationship("DaySchedule", back_populates="user")
    groups = relationship("Group", secondary="groupUsers", back_populates="users")


class Profile(Base):
    __tablename__ = "profiles"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    lastname = Column(String, nullable=False)
    role = Column(Enum(Role))
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="profile")
