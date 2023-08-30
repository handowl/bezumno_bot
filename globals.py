from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from decouple import config

bot = Bot(token=config("BOT_API"))
dp = Dispatcher(bot)
