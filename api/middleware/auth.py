from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
import os

class AuthMiddleware(BaseHTTPMiddleware):
    """Simple API key authentication middleware."""
    async def dispatch(self, request: Request, call_next):
        api_key_header = os.getenv("API_KEY_HEADER", "X-API-Key")
        expected_key = os.getenv("API_KEY", "dev-key")
        
        if request.url.path in ["/", "/health", "/docs", "/openapi.json"]:
            return await call_next(request)
        
        api_key = request.headers.get(api_key_header)
        if api_key != expected_key:
            from fastapi.responses import JSONResponse
            return JSONResponse(
                status_code=401,
                content={"error": "Invalid API key"}
            )
        
        return await call_next(request)
