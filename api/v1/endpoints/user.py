# Contains API endpoints, versioning, and dependency injection.

from fastapi import APIRouter
from schemas import UserCreate,UserResponse
from services import create_user
router = APIRouter()

@router.post("/", response_model=UserResponse)
def register_user(user: UserCreate):
    try:
        return create_user(user)
    except Exception as e:
        print("Lỗi khác:", e)
