
from models.user import User
from sqlalchemy.orm import Session
from schemas import UserCreate
from sqlalchemy.exc import IntegrityError
from fastapi import HTTPException, status

# Encapsulates business logic and interacts with the database.
def create_user(user_data:UserCreate,db:Session):
    try:
        new_user = User(username=user_data.username,email=user_data.email,password=user_data.password)
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

def get_users(db:Session):
    try:
        users = db.query(User).all()
        if len(users):
            return users
        return []
    except Exception as e:
        print('e:',e)