from aiogram import Bot, Dispatcher

from .config import load_bot


conf = load_bot()

bot = Bot(token="8323816529:AAFH5VCvK-qZM3eeG50QJj_Rkouwco8993M")
dp = Dispatcher()

