from aiogram import types
from aiogram.dispatcher.filters.builtin import Command

from loader import dp
from keyboards.default.menu_kb import menu_keyboards


@dp.message_handler(Command('menu'))
async def command_menu(message: types.Message):
    await message.answer("Menu bo'limi: ", reply_markup=menu_keyboards)

#
# @dp.message_handler(commands=['menu', 'menyu', ])
# async def command_menu(message: types.Message):
#     await message.answer("Menu bo'limi: ", reply_markup=menu_keyboards)
#

# /start
# /help
# /contact
# /about
# /setting
