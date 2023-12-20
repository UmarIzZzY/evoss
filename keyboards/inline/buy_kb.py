from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

buy_product = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
    [
        InlineKeyboardButton('🛒 Savatga qo\'shish', callback_data='savatga_qoshish'),
        InlineKeyboardButton('🔙 Orqaga', callback_data='orqaga'),
    ]
])

buy_product_new = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton('Sotib olish', callback_data='buy_product_new')
    ]
])
