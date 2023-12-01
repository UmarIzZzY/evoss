from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton

start_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('🍴 Menu')],
    [KeyboardButton('🛍 Mening zakazlarim')],
    [KeyboardButton('✍️ Ariza qoldirish'), KeyboardButton('⚙️ Sozlamalar')]
])

contact = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('📞 Telefon raqam yuborish', request_contact=True)]
])