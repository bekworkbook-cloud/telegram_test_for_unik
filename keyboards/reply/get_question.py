from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


kb = [
    [KeyboardButton(text="Задать вопрос")]
]

markup = ReplyKeyboardMarkup(
    keyboard=kb,
)