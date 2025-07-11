# Contains API endpoints, versioning, and dependency injection.

from fastapi import APIRouter,Depends
from schemas import UserRead,UserCreate
from services import get_users,create_user
from db.deps import get_db
from sqlalchemy.orm import Session
router = APIRouter()

@router.get("/", response_model=list[UserRead])
def get_all_users(db: Session = Depends(get_db)):
    return get_users(db) or []


@router.post("/",response_model=UserCreate)
def register_user(user: UserCreate,db: Session = Depends(get_db)):
    return create_user(user,db)
