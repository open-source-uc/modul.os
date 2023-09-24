from fastapi import APIRouter

import schemas

router = APIRouter(prefix="/users", tags=["users"])


@router.post("/", response_model=schemas.User)
def create_user(
):
    """
    Create new user.
    """
    pass


@router.get("/{id}", response_model=schemas.User)
def read_user():
    """
    Get user by ID.
    """
    pass


@router.put("/{id}", response_model=schemas.User)
def update_user():
    """
    Update a user.
    """
    pass


@router.delete("/{id}", response_model=schemas.User)
def delete_user():
    """
    Delete a user.
    """
    pass


@router.get("/", response_model=list[schemas.User])
def read_users():
    """
    Get all users.
    """
    return {"test": "users list"}
