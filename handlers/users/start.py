from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart, Command, IDFilter

from data.config import ADMINS
from keyboards.default.start_kb import start_keyboards, contact
from loader import dp
from states.users import RegisterState
from utils.db_api.start_db import insert_user, select_user


@dp.message_handler(CommandStart(), IDFilter(chat_id=ADMINS))
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}! Xush kelibsiz aka",
                         reply_markup=start_keyboards)


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if select_user(message.from_user.id):
        await message.answer(f"Salom, {message.from_user.full_name}! Evos botimizga xush kelibsiz",
                             reply_markup=start_keyboards)
    else:
        await message.answer("Botdan foydalanish uchun Registratsiyadan o'ting!\nIsm Familiyangizni kiriting:")
        await RegisterState.full_name.set()


@dp.message_handler(state=RegisterState.full_name)
async def full_name(message: types.Message, state: FSMContext):
    await state.update_data(full_name=message.text)
    await message.answer("Nechi yoshdasiz: ")
    await RegisterState.next()


@dp.message_handler(state=RegisterState.age)
async def full_name(message: types.Message, state: FSMContext):
    await state.update_data(age=message.text)
    await message.answer("Telefon raqamingiz: ", reply_markup=contact)
    await RegisterState.next()


@dp.message_handler(state=RegisterState.phone_number, content_types=types.ContentTypes.CONTACT)
async def full_name(message: types.Message, state: FSMContext):
    await state.update_data(phone_number=message.contact.phone_number, user_id=message.from_user.id)

    data = await state.get_data()
    insert_user(data)

    await message.answer("Tabriklaymiz! Siz ro'yxatdan o'tdingiz!", reply_markup=start_keyboards)
    await state.finish()
