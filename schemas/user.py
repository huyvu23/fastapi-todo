# Defines Pydantic models for request validation and response serialization.
from pydantic import BaseModel,Field
from datetime import datetime

class UserLogin(BaseModel):
    username:str = Field(min_length=5,max_length=50)
    password: str

# Schema để đọc dữ liệu người dùng (ví dụ: trả về từ API)
class UserBase(BaseModel):
    username: str = Field(min_length=5,max_length=50)
    email: str

# Schema để tạo người dùng mới (POST request)
class UserCreate(UserBase):
    password: str

class UserUpdate(BaseModel):
    email:str

# Schema để trả về dữ liệu người dùng (GET response)
class UserRead(UserBase):
    id: int
    created_at: datetime

    class Config:
        from_attributes = True  # Cho phép đọc dữ liệu từ SQLAlchemy model

class InformationUserLogin(UserRead):
    access_token:str