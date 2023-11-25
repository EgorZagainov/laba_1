import asyncio
import logging
import sys

from handlers import cmd_inline, cmd_random
from loader import dp, bot


async def main() -> None:

    dp.message.register(cmd_random)
    dp.message.register(cmd_inline)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
