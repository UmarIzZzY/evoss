from aiogram import types
from aiogram.dispatcher.filters import Text, Comm
from keyboards.default.menu_kb import menu_keyboards
from loader import dp


@dp.message_handler(Text(equals="🍴 Menu"))
@dp.message_handler(lambda message: message.text == "🍴 Menu")
async def menu(message: types.Message):
    await message.answer("Menu bo'limi", reply_markup=menu_keyboards)


@dp.message_handler(Text(contains='salom'))
async def sub_menu(message: types.Message):
    await message.answer("Va aleykum assalom")


# contains, startwith, endwith='?'
@dp.message_handler(Text(contains='ahmoq'))
async def sub_menu(message: types.Message):
    await message.answer("O'zin shunaqasan")
