import asyncio
import logging
import sys
import os

from aiogram import Bot, Dispatcher, types, Router, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import Command, CommandStart

from dotenv import load_dotenv

from handlers import router


#----------- ------------------
async def main():
    load_dotenv()
    TOKEN = os.getenv("TOKEN")
    print(TOKEN)

    bot = Bot(
        token=TOKEN,
        default=DefaultBotProperties(parse_mode=ParseMode.HTML),
    )
    dp = Dispatcher()
    dp.include_router(router)
    print('Бот успішно запущений')
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот зупинено')