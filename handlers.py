from aiogram import types
from aiogram.types import MenuButtonWebApp, WebAppInfo
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

async def start_handler(message: types.Message):
    bot = message.bot
    chat_id = message.chat.id
    webapp_info = WebAppInfo(url="https://handowl.github.io/")
    button = MenuButtonWebApp("Заказ", webapp_info)

    await bot.set_chat_menu_button(chat_id, button)