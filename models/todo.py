from sqlalchemy import Column, Integer, String,DateTime,func,ForeignKey,Boolean
from sqlalchemy.orm import relationship
from db.session import Base

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True,autoincrement=True)
    user_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"))
    title = Column(String(255), nullable=False)
    description = Column(String(1000))
    is_completed = Column(Boolean, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    update_at = Column(DateTime(timezone=True), server_default=func.now(),onupdate=func.now())

    owner = relationship("User", back_populates="todos")
    
