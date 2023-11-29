from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart, Command, IDFilter

from data.config import ADMINS
from keyboards.default.start_kb import start_keyboards
from loader import dp


@dp.message_handler(CommandStart(), IDFilter(chat_id=ADMINS))
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! Xush kelibsiz aka",
                         reply_markup=start_keyboards)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! Evos botimizga xush kelibsiz",
                         reply_markup=start_keyboards)
