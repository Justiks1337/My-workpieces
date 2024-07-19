import asyncio

from aiogram.filters import CommandStart
from aiogram.types import Message

from initializer import dp, bot


dp.message(CommandStart())


async def start_command_handler(message: Message):
    pass


async def main():
    await dp.start_polling(bot)



if __name__ == '__main__':
    asyncio.run(main())