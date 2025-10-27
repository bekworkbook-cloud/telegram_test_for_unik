import re
import html

from aiogram import Router, F
from aiogram.types import Message
from data.get_data import get_data, get_nasty_data
from utils.find_question import find
from utils.random_question import get_random_question

router = Router()


@router.message(F.text == "Задать вопрос")
async def handle_random_question(msg: Message):
    # data = await get_data()
    data = await get_nasty_data()
    q = await get_random_question(data)  # await imported coroutine
    if " == " in q:
        question, answer = q.split(" == ", 1)
    else:
        question, answer = q, "Нет ответа"
    await msg.answer(
        f"<b>Вопрос</b>: {html.escape(question)}\nОтвет: <tg-spoiler>{html.escape(answer)}</tg-spoiler>",
        parse_mode="HTML"
    )


@router.message(F.text)
async def ask_question(msg: Message):
    text = msg.text
    # data = await get_data()
    data = await get_nasty_data()
    result = await find(text, data)
    if not result:
        await msg.reply("Извините, я не смог найти ответ на ваш вопрос.")
        return

    for i in result:
        question, sep, answer = i.partition(" == ")
        if not sep:
            continue
        content = f"<b>Вопрос:</b> {html.escape(question)} \n<b>Ответ:</b> <tg-spoiler>{html.escape(answer)}</tg-spoiler>"
        await msg.bot.send_message(
            chat_id=msg.chat.id,
            text=content,
            parse_mode="HTML"
        )
