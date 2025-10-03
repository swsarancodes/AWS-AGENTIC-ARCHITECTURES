from fastapi import APIRouter

router = APIRouter(prefix="/health", tags=["health"])

@router.get("")
def health_check():
    return {"status": "healthy", "service": "AWS Agentic Architectures API"}
