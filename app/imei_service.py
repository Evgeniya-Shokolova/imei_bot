import httpx
import os

from dotenv import load_dotenv
load_dotenv()

API_URL = "https://imeicheck.net/api/check"
API_TOKEN = os.getenv('TOKEN')


def check_imei(imei: str):
    """Проверка IMEI на сервисе"""
    response = httpx.post(API_URL, json={"imei": imei, "token": API_TOKEN})

    if response.status_code == 200:
        return True, response.join()
    return False, None