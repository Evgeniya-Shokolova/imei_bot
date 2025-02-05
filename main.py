import asyncio
from fastapi import FastAPI
from app.api import router as api_router
from app.bot import start_bot

# Создаем объект FastAPI
app = FastAPI()
# Подключаем маршруты
app.include_router(api_router)


@app.get("/")
def read_root():
    return {"message": "Добро пожаловать! FastAPI работает!"}

@app.on_event("startup")
async def on_startup():
    """Запуск бота"""
    asyncio.create_task(start_bot())
