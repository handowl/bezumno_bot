from aiogram.utils import executor

from handlers import *
from globals import dp

async def on_startup(_):
    print("Started")


dp.register_message_handler(start_handler, commands=["start"])

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)