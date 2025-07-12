# Contains API endpoints, versioning, and dependency injection.

from fastapi import APIRouter,Depends
from schemas import UserRead,UserCreate
from services import delete_user,get_users,create_user,get_users_according_id
from db.deps import get_db
from sqlalchemy.orm import Session

router = APIRouter()

@router.get("/", response_model=list[UserRead])
def get_all_users(db: Session = Depends(get_db)): ## Depends(get_db) dùng để lấy ra 1 session từ DB và tiêm vào hàm xử lý route.
    return get_users(db) or []

@router.post("/",response_model=UserCreate)
def register_user(user: UserCreate,db: Session = Depends(get_db)):
    return create_user(user,db)

@router.get("/{id}", response_model=UserRead)
def get_user_by_id(id:int,db: Session = Depends(get_db)):
    return get_users_according_id(id,db)

@router.delete("/{id}", status_code=204)
def delete_user_by_id(id:int,db: Session = Depends(get_db)):
    return delete_user(id,db)