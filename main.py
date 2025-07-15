from fastapi import FastAPI
from api.v1.endpoints import user,todo,auth
from middleware.auth_middleware import AuthMiddleware

app = FastAPI(version="1.0.0")
app.add_middleware(AuthMiddleware)

# tags=["users"]: tất cả các endpoint bên trong user.router sẽ được nhóm lại thành "users" trong Swagger UI.
app.include_router(user.router, prefix="/api/v1/users", tags=["users"])
app.include_router(todo.router, prefix="/api/v1/todos", tags=["todos"])
app.include_router(auth.router, prefix="/api/v1/auth", tags=["auth"])