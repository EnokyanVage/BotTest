from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, Message

from loader import dp


async def change_stop(message: Message):
    await message.answer("Остановил.",reply_markup=del_keyb)

del_keyb = ReplyKeyboardRemove()

kb_menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='good!'),
            KeyboardButton(text='mood!'),
        ],
        [
            KeyboardButton(text='Стоп'),
        ]
    ],
    resize_keyboard=True
)