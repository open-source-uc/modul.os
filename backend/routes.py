from fastapi import APIRouter

api_router = APIRouter()


@api_router.get("/hello")
async def read_hello():
    """
    Endpoint de ejemplo "Hola Mundo"
    """
    return {"message": "Hola Mundo"}
