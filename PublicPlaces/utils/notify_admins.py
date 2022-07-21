import logging

from aiogram import Dispatcher

from data.config import admin

async def on_startup_notify(dp: Dispatcher):
    for admin_id in admin:
        try:
            text = 'Бот запущен!'
            await dp.bot.send_message(chat_id=admin_id, text=text)
        except Exception as arr:
            logging.exception(arr)