from aiogram import types


from loader import dp


@dp.message_handler(content_types='photo')
@dp.message_handler(content_types=types.ContentType.STICKER)
async def photo_get(message: types.Message):
    await message.answer("Bu qanday rasm yoki sticker?")
