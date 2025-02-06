import os
from aiogram import Bot, Dispatcher
from aiogram.types import Message

import requests

from app.whitelist import is_user_allowed
from dotenv import load_dotenv


load_dotenv()

BOT_TOKEN = os.getenv('BOT_TOKEN')
SANDBOX_API_URL = os.getenv('SANDBOX_API_URL')
API_SANDBOX_TOKEN = os.getenv('API_SANDBOX_TOKEN')

# Инициализация бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def is_valid_imei(imei: str) -> bool:
    """Проверяет, является ли строка корректным IMEI (15 цифр)."""
    return imei.isdigit() and len(imei) == 15


@dp.message()
async def handle_imei(message: Message):
    """Обработчик сообщений"""
    user_id = message.from_user.id

    # Проверка пользователя в списке доступа
    if not is_user_allowed(user_id):
        await message.reply('У вас нет доступа к использованию этого бота.')
        return

    imei = message.text.strip()

    # Проверка IMEI
    if not is_valid_imei(imei):
        await message.reply('Некорректный IMEI. Попробуйте снова!')
        return

    # Обращение к API для проверки IMEI
    headers = {'Authorization': f'{API_SANDBOX_TOKEN}'}
    response = requests.post(SANDBOX_API_URL,
                             json={'imei': imei}, headers=headers)

    if response.status_code == 200:
        imei_data = response.json()
        await message.reply(f'Информация об IMEI:\n{imei_data}')
    else:
        await message.reply(
            f'Ошибка при проверке IMEI (код: {response.status_code})')


async def start_bot():
    """Главная функция для запуска бота"""
    try:
        # Запуск диспетчера
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
