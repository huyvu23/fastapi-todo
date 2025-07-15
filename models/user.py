from sqlalchemy import Column, Integer, String,DateTime,func,UniqueConstraint
from db.session import Base
from sqlalchemy.orm import relationship

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False) 
    created_at = Column(DateTime(timezone=True), server_default=func.now())

    # all:Bao gồm tất cả hành động: save-update, merge, delete, refresh-expire, expunge 
    # delete-orphan:Khi một Todo không còn gắn với User nào, thì tự động bị xóa khỏi DB
    # back_populates là tên thuộc tính bạn tự đặt, miễn là Tên đó khớp giữa hai model
    todos = relationship("Todo", back_populates="owner", cascade="all, delete-orphan")
    ## Là thuộc tính đặc biệt trong SQLAlchemy được dùng để cấu hình các ràng buộc (constraints) và tùy chọn cho bảng (table).
    __table_args__ = (
        UniqueConstraint('email', name='uq_user_email'),
        UniqueConstraint('username', name='uq_user_username'),
    )
