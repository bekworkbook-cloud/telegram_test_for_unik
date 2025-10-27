from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command, CommandStart

from keyboards.reply.get_question import markup




router = Router()


@router.message(CommandStart())
async def cmd_start(msg: Message):
    await msg.answer("Hello man", reply_markup=markup)


@router.message(Command(commands=["help"]))
async def cmd_help(msg: Message):
    await msg.answer("This is help message")


@router.message(Command(commands=["about"]))
async def cmd_mode(msg: Message):
    await msg.answer("Bot mode changed")
