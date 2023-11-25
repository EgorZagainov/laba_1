from random import randint

from aiogram.filters import CommandStart,Command
from aiogram.utils.markdown import hbold
from aiogram.types import Message
from loader import dp
from aiogram import types, Bot, F
from aiogram.utils.keyboard import InlineKeyboardBuilder



@dp.message(CommandStart())
async def cmd_start(message: Message) -> None:
    kb = [
        [types.KeyboardButton(text='Я программист'),
         types.KeyboardButton(text='Я человек')],
        [types.KeyboardButton(text='Я не знаю кто я')],
    ]
    keyboard = types.ReplyKeyboardMarkup(
        keyboard=kb,
        resize_keyboard=True)

    await message.answer(f'Hello ,{hbold(message.from_user.full_name)}', reply_markup=keyboard)



@dp.message(Command("inline"))
async def cmd_inline(message: Message, bot: Bot):
    builder = InlineKeyboardBuilder()
    builder.row(types.InlineKeyboardButton(
        text="GitHub", url="https://github.com")
        )
    builder.row(types.InlineKeyboardButton(
        text="Оф. канал Telegram",
        url="tg://resolve?domain=telegram")
        )
    await message.answer(
        'Выберите ссылку', reply_markup=builder.as_markup(),
    )

@dp.message(Command("random"))
async def cmd_random(message: types.Message):
    builder = InlineKeyboardBuilder()
    builder.add(types.InlineKeyboardButton(
        text="Нажми меня",
        callback_data="random_value")
    )
    await message.answer(
        "Нажмите на кнопку, чтобы бот отправил число от 1 до 100000",
        reply_markup=builder.as_markup()
    )
@dp.callback_query(F.data == "random_value")
async def send_random_value(callback: types.CallbackQuery):
    await callback.message.answer(str(randint(1, 100000)))
    await callback.answer()




