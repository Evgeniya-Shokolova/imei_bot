import httpx
import os
from dotenv import load_dotenv

# Загрузка переменных окружения
load_dotenv()

# Конфигурация из .env
API_URL = os.getenv('URL')
API_TOKEN = os.getenv('TOKEN')


def check_imei(imei: str):
    """Проверка IMEI на внешнем сервисе."""
    response = httpx.post(API_URL, json={'imei': imei, 'token': API_TOKEN})
    if response.status_code == 200:
        return True, response.json()
    return False, None
