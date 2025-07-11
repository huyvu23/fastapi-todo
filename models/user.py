from sqlalchemy import Column, Integer, String,DateTime,func,UniqueConstraint
from db.session import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    ## Là thuộc tính đặc biệt trong SQLAlchemy được dùng để cấu hình các ràng buộc (constraints) và tùy chọn cho bảng (table).
    __table_args__ = (
        UniqueConstraint('email', name='uq_user_email'),
        UniqueConstraint('username', name='uq_user_username'),
    )
