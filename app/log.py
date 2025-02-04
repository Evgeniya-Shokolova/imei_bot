import logging
import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (CommandHandler, CallbackContext, filters,
                          MessageHandler, ApplicationBuilder)
from fastapi import FastAPI
from app.imei_service import check_imei
from app.whitelist import is_user_allowed


load_dotenv()
TOKEN = os.getenv('TELEGRAM_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def start(update: Update, context: CallbackContext):
    """Начало работы бота"""
    update.message.reply_text('Отправьте IMEI для проверки')


def handle_imei(update: Update, context: CallbackContext):
    """Обработка IMEI"""
    user_id = update.message.from_user.id
    imei = update.message.text

    if not is_user_allowed(user_id):
        update.message.reply_text('У вас нет доступа.')
        return

    valid, data = check_imei(imei)
    if valid:
        update.message.reply_text(f'Информация о IMEI: {data}')
    else:
        update.message.reply_text('Недействительный IMEI')


def start_bot():
    """Запуск бота"""
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler('start', start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,
                                           handle_imei))

    application.run_polling()


app = FastAPI()

if __name__ == "__main__":
    start_bot()
