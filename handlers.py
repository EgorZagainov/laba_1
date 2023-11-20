from aiogram.filters import Command, CommandStart
from aiogram.utils.markdown import bold
from aiogram import types
from loader import dp


@dp.message(CommandStart())
async def cmd_start(message: types.Message) -> None:
    await message.answer(f'Hello,{bold(message.from_user.full_name)}')


@dp.message()
async def echo_handler(message: types.Message) -> None:
    try:

        await message.send_copy(chat_id=message.chat.id)

    except TypeError:
        await message.answer('ОШИБКА')






