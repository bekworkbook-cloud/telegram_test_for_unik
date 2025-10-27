import asyncio

from config.load import bot, dp
from handlers.user import router as user_router
from handlers.commands import router as cmd_router
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)
logging.getLogger("aiogram").setLevel(logging.INFO)


async def main():

    
    dp.include_router(cmd_router)
    dp.include_router(user_router)
    await dp.start_polling(bot)


if __name__=="__main__":
    asyncio.run(main())
