from fastapi import APIRouter
from app.models.password_models import PasswordAnalyzeRequest, PasswordAnalyzeResponse
from app.services.password_service import password_service

router = APIRouter(
    prefix="/api/password",
    tags = ["password"]
)


@router.post("/analyze",response_model=PasswordAnalyzeResponse)
def analyze_password(request: PasswordAnalyzeRequest):
    return password_service.analyze_password(request.password)