# Contains API endpoints, versioning, and dependency injection.

from fastapi import APIRouter
from schemas import UserRead,UserUpdate
from services import edit_user,delete_user,get_users,get_users_according_id
from db.deps import SessionDep

router = APIRouter()

@router.get("/", response_model=list[UserRead])
def get_all_users(db: SessionDep): ## Depends(get_db) dùng để lấy ra 1 session từ DB và tiêm vào hàm xử lý route.
    return get_users(db) or []

@router.get("/{id}", response_model=UserRead)
def get_user_by_id(id:int,db: SessionDep):
    return get_users_according_id(id,db)

@router.delete("/{id}", status_code=204)
def delete_user_by_id(id:int,db: SessionDep):
    return delete_user(id,db)

@router.put("/{user_id}", response_model=UserRead)
def update_user(user_id: int, update_data: UserUpdate, db: SessionDep):
    return edit_user(user_id,update_data,db)