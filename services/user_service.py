
from models.user import User
from sqlalchemy.orm import Session
from schemas import UserCreate,UserLogin,UserRead,UserUpdate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status
from core import hash_password,verify_password

# Encapsulates business logic and interacts with the database.
def create_user(user_data:UserCreate,db:Session):
    try:
        value_hash_password = hash_password(user_data.password)
        new_user = User(username=user_data.username,email=user_data.email,password=value_hash_password)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
    except IntegrityError as e:
        ## Hủy bỏ toàn bộ những thay đổi đang chờ được commit trong session hiện tại.
        db.rollback()

        ## Trích xuất thông báo lỗi gốc (ngắn gọn và chi tiết hơn) từ đối tượng lỗi
        error_message = str(e.orig)
        if 'users_email_key' in error_message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already exists"
            )
        elif 'users_username_key' in error_message:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exists"
            )

        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Internal server error"
        )

def get_users_according_id(id:int,db:Session) -> UserRead:
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

def delete_user(id:int,db:Session):
    user = db.query(User).filter(User.id == id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    db.delete(user)
    db.commit()
    return

def edit_user(user_id: int, update_data: UserUpdate, db: Session) -> UserCreate:
    user = db.query(User).filter(User.id == user_id).first()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    # Check and update fields
    if update_data.email is not None:
        user.email = update_data.email

    try:
        db.commit()
        db.refresh(user)
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=400, detail=str(e.orig) if hasattr(e, 'orig') else "Update failed")

    return user

def get_users(db:Session) -> list[UserCreate]:
    try:
        users = db.query(User).all()
        if len(users):
            return users
        return []
    except Exception as e:
        print('e:',e)

def verify_user_login(db: Session, login_data: UserLogin) -> UserRead | None:
    try:
        user = db.query(User).filter(User.username == login_data.username).first()
        if not user:
            raise HTTPException(status_code=400, detail="Invalid email or password")

        if not verify_password(login_data.password, user.password):
            raise HTTPException(status_code=400, detail="Invalid password")
        return user
    except Exception as e:
        print('e:',e)

    