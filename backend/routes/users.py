from fastapi import APIRouter, Path
from pydantic import BaseModel
from typing import List

user_router = APIRouter()

users = []
"""
Lista de usuarios, mientras no tengamos una base de datos
"""

class User(BaseModel):
    """
    Usuarios: nombre, email, password
    """
    name: str
    email: str
    password: str

@user_router.get("/hello")
async def read_hello():
    """
    Endpoint de ejemplo "Hola Mundo"
    """
    return {"message": "Hola Mundo"}

@user_router.get("/users", response_model=List[User])
async def get_users():
    """
    Endpoint para obtener todos los usuarios
    """
    return users

@user_router.post("/users")
async def create_user(user: User):
    """
    Endpoint para crear un usuario
    """
    users.append(user)
    return {"message":
             f"Usuario {user.name} creado exitosamente"}

@user_router.get("/users/{user_id}")
async def get_user(user_id: int = Path(..., description="ID del usuario", ge=0)):
    """
    Endpoint para obtener un usuario por su id
    """
    return users[user_id]
