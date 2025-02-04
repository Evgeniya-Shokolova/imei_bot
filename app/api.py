from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from app.imei_service import check_imei


router = APIRouter()


class CheckIMEIRequest(BaseModel):
    """Модель для проверки IMEI"""
    imei: str
    token: str

@router.post("/api/check-imei")
async def check_imei_api(request: CheckIMEIRequest):
    """Проверка IMEI через API"""
    if not validate_token(request.token):
        raise HTTPException(status_code=403, detail='invalid token')

    valid, data = check_imei(request.imei)
    if valid:
        return {'succes': True, 'data': data}
    else:
        raise HTTPException(status_code=400, detail='invalid IMEI')
