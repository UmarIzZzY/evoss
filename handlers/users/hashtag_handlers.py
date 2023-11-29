from aiogram import types
from aiogram.types import InputFile

from loader import dp


@dp.message_handler(hashtags='uzb')
async def uzb_hashtag(message: types.Message):
    rasm = InputFile('images/uzbekistan-flag.jpg')
    await message.answer_photo(photo=rasm, caption='UZB flag')


@dp.message_handler(cashtags='USD')
async def uzb_hashtag(message: types.Message):
    rasm = InputFile('images/uzbekistan-flag.jpg')
    await message.answer_photo(photo=rasm, caption='UZB flag')
