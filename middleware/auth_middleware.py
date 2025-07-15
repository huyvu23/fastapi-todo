from fastapi import Request, HTTPException
from starlette.middleware.base import BaseHTTPMiddleware ## base class để viết custom middleware
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
from core.security import decode_access_token
from fastapi.responses import JSONResponse

security = HTTPBearer(auto_error=False)

class AuthMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            path = request.url.path
            # Skip auth for public routes
            if path.startswith("/api/v1/auth"):
                return await call_next(request)

            # Extract token
            credentials: HTTPAuthorizationCredentials = await security(request)
            # print("credentials:",credentials)
            if not credentials:
                raise HTTPException(status_code=401, detail="Missing Authorization Header")

            token = credentials.credentials
            payload = decode_access_token(token)
            if not payload:
                raise HTTPException(status_code=401, detail="Invalid or expired token")

            # Attach user to request for later use
            request.state.user = payload
            return await call_next(request)
        except HTTPException as e:
            # Trả lỗi dạng JSON như FastAPI vẫn làm
            return JSONResponse(
            status_code=e.status_code,
            content={"detail": e.detail},
        )
        except Exception as e:
            # Các lỗi khác không phải HTTPException
            return JSONResponse(
            status_code=500,
            content={"detail": "Internal server error"},
        )
