import os

from dotenv import load_dotenv
from aiogram import Dispatcher, Bot


load_dotenv(".env")


bot = Bot(os.getenv("BOT_TOKEN"))
dp = Dispatcher()
