import asyncio
import logging
import sys

from aiogram import Bot
from config import TOKEN
from handlers import cmd_start
from loader import dp
from aiogram.enums import ParseMode



async def main () -> None:
    dp.message.register(cmd_start)
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())