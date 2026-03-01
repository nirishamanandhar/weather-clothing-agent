import os
from fastapi import HTTPException, status, Depends
from fastapi.security import APIKeyHeader

API_KEY = os.getenv("BACKEND_AUTH_TOKEN")
api_key_header = APIKeyHeader(name="x-api-key", auto_error=False)


async def verify_backend_token(api_key: str = Depends(api_key_header)):
    if API_KEY is None:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Auth token not configured on server",
        )

    if api_key != API_KEY:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
        )
