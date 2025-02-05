import os
from fastapi import APIRouter, HTTPException, Header
from pydantic import BaseModel
import requests
from dotenv import load_dotenv

load_dotenv()

# Конфигурация окружения
SANDBOX_API_URL = os.getenv('SANDBOX_API_URL')
SANDBOX_API_TOKEN = os.getenv('API_TOKEN')
API_TOKEN = os.getenv('TOKEN')

router = APIRouter()


class IMEIRequest(BaseModel):
    """Модель данных для API запроса"""
    imei: str
    token: str


def check_auth_token(token: str):
    """Авторизация через токен"""
    if token != API_TOKEN:
        raise HTTPException(status_code=401, detail='Unauthorized')
    return True


def check_imei(imei: str) -> dict:
    """Проверка IMEI через внешний API"""
    headers = {'Authorization': f'{SANDBOX_API_TOKEN}'}
    response = requests.post(SANDBOX_API_URL, json={'imei': imei},
                             headers=headers)
    if response.status_code != 200:
        raise HTTPException(status_code=response.status_code,
                            detail='Ошибка проверки IMEI')
    return response.json()


@router.post('/api/check-imei')
def api_check_imei(request: IMEIRequest,
                   token: str = Header(
                       lambda: check_auth_token(requests.token))):
    """Эндпоинт для проверки IMEI"""
    check_auth_token(token)
    imei_data = check_imei(request.imei)
    return {'success': True, 'data': imei_data}

