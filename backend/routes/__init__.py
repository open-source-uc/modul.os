"""
Las rutas se agrupan bajo este módulo.
"""
from fastapi import APIRouter

from routes import hello, users

api_router = APIRouter()

api_router.include_router(hello.router,prefix="/hello", tags=["hello"])
api_router.include_router(users.router,prefix="/users", tags=["users"])
