# Contains API endpoints, versioning, and dependency injection.

from fastapi import APIRouter,Depends
from schemas import UserCreate,UserRead
from services import create_user,get_users
from db.deps import get_db
from sqlalchemy.orm import Session
router = APIRouter()

@router.get("/", response_model=list[UserRead])
def get_all_users(db: Session = Depends(get_db)):
    try:
        return get_users(db) or []
    except Exception as e:
        print("error:",e)

# @router.post("/", response_model=UserRead)
# def register_user(user: UserCreate):
#     return create_user(user)

