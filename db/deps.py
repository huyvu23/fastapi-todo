from db.session import SessionLocal
from typing import Annotated
from fastapi import Depends
from sqlalchemy.orm import Session

def get_db():
    db = SessionLocal()  # Tạo một phiên (session) kết nối đến cơ sở dữ liệu
    try:
        yield db  # Trả về session này để dùng trong các hàm xử lý (vd: route của FastAPI)
    finally:
        db.close()  # Đảm bảo đóng session sau khi xong việc, dù có lỗi hay không

## Annotated[T, M]
## T : Type chính mà biến đang mang (kiểu dữ liệu gốc)
## M : Metadata bổ sung (dành cho thư viện như FastAPI xử lý thêm)
SessionDep = Annotated[Session, Depends(get_db)]
