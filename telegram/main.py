import asyncio
import os

from dotenv import load_dotenv
from aiogram import Bot

from telegram.dispatcher import dp


load_dotenv()


async def main():
    bot = Bot(os.getenv("BOT_TOKEN"))
    # import telegram.handlers  # load handlers
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
