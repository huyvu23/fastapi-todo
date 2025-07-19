## Tóm tắt

Python 3 có nhiều cải tiến so với Python 2, bao gồm cú pháp mới, thay đổi cách chia, cải tiến Unicode, và thay đổi trong thư viện chuẩn.

pip là công cụ cài đặt gói cho Python, và pip3 được sử dụng khi bạn làm việc với Python 3.

Nếu bạn sử dụng Python 2, bạn dùng pip, và nếu bạn sử dụng Python 3, bạn dùng pip3.

Lưu ý: Python 2 đã ngừng hỗ trợ chính thức từ tháng 1 năm 2020, vì vậy bạn nên sử dụng Python 3 cho các dự án mới.

## Tạo Virtual Environment

- python3 -m venv .venv

## Sử dụng venv cho dự án

- source .venv/bin/activate

## Cài đặt các dependencies bằng pip3

- pip3 install -r requirements.txt

## Tạo ra file requirements.txt để chứa các dependency của dự án

- pip3 freeze > requirements.txt

## Lệnh chạy dự án

- uvicorn main:app --reload

## Lệnh chạy migration

-> Câu lệnh dưới có tác dụng Tạo file migration tự động

- alembic revision --autogenerate -m "change config column description"

-> Câu lệnh dưới có tác dụng Áp dụng migration vào DB

- alembic upgrade head

## Các package sử dụng để kết nối với database

- sqlalchemy: Là ORM (Object-Relational Mapping) cho phép bạn làm việc với cơ sở dữ liệu SQL một cách trừu tượng, không cần viết SQL thủ công.

- asyncpg: Thư viện kết nối PostgreSQL nhanh và hiệu quả, sử dụng async/await để tối ưu hóa kết nối.

- databases: Là thư viện hỗ trợ kết nối và truy vấn cơ sở dữ liệu một cách bất đồng bộ (asynchronous), giúp tăng hiệu suất khi làm việc với các cơ sở dữ liệu như PostgreSQL.

## Tại sao lại cần một session mỗi lần thao tác với DB

- Isolation : Đảm bảo mỗi request là độc lập
- Connection Safety : Không giữ kết nối mở gây tốn tài nguyên
- Transaction Control : Hỗ trợ rollback/Commit đúng cách
- Best Practice : Theo đúng kiến trúc RESTful và Fast API chuẩn

## Chạy test từ thư mục gốc của project (fastapi-todo) bằng lệnh sau

- PYTHONPATH=. pytest

## CONNECT DB

- DATABASE_URI = 'postgresql://postgres:<password>@localhost/<name_of_the_datbase>'

<!-- RECOMMEND PROJECT STRUCTURE -->
<!-- https://www.linkedin.com/pulse/fastapi-project-structure-best-practices-manikandan-parasuraman-fx4pc/ -->

project_name/
│
├── app/
│ ├── **init**.py
│ ├── main.py
│ ├── api/
│ │ ├── **init**.py
│ │ ├── v1/
│ │ │ ├── **init**.py
│ │ │ ├── endpoints/
│ │ │ │ ├── **init**.py
│ │ │ │ ├── user.py
│ │ │ │ ├── auth.py
│ │ │ │ ├── item.py
│ │ ├── dependencies/
│ │ ├── **init**.py
│ │ ├── database.py
│ │ ├── auth.py
│ │
│ ├── core/
│ │ ├── **init**.py
│ │ ├── config.py
│ │ ├── security.py
│ │
│ ├── db/
│ │ ├── **init**.py
│ │ ├── base.py
│ │ ├── models/
│ │ │ ├── **init**.py
│ │ │ ├── user.py
│ │ │ ├── item.py
│ │ ├── session.py
│ │
│ ├── schemas/
│ │ ├── **init**.py
│ │ ├── user.py
│ │ ├── item.py
│ │
│ ├── services/
│ │ ├── **init**.py
│ │ ├── user_service.py
│ │ ├── item_service.py
│ │
│ ├── tests/
│ ├── **init**.py
│ ├── test_user.py
│ ├── test_item.py
│
├── Dockerfile
├── docker-compose.yml
├── .env
├── requirements.txt
├── README.md
