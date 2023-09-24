from fastapi import APIRouter

router = APIRouter(prefix="/hello", tags=["hello"])


@router.get("/")
async def read_hello():
    """
    Endpoint de ejemplo "Hola Mundo"
    """
    return {"message": "Hola Mundo"}