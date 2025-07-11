from db.session import SessionLocal

def get_db():
    db = SessionLocal()  # Tạo một phiên (session) kết nối đến cơ sở dữ liệu
    try:
        yield db  # Trả về session này để dùng trong các hàm xử lý (vd: route của FastAPI)
    finally:
        db.close()  # Đảm bảo đóng session sau khi xong việc, dù có lỗi hay không
