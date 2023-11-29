from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('🍴 Menu')],
    [KeyboardButton('🛍 Mening zakazlarim')],
    [KeyboardButton('✍️ Ariza qoldirish'), KeyboardButton('⚙️ Sozlamalar')]
])

contact = ReplyKeyboardMarkup().add(KeyboardButton('Telefon raqam jonatish', request_contact=True))