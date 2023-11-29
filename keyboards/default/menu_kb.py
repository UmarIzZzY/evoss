from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

menu_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [KeyboardButton('🌯 Lavash'), KeyboardButton('🌭 Hot dog')],
    [KeyboardButton('🌮 Taco'), KeyboardButton('🍔 Burger')],
    [KeyboardButton('🍕 Pizza'), KeyboardButton('🥩 Steyk')],
    [KeyboardButton('🍦 Muzqaymoq'), KeyboardButton('🎂 Tort')],
    [KeyboardButton('🍟 Kartoshka Fri')],
    [KeyboardButton('🔙 Bosh sahifa')]
])

lavash_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, keyboard=[
    [
        KeyboardButton('🌯 mini lavash'),
        KeyboardButton('🌯 big lavash'),
    ],
    [
        KeyboardButton('🌯 mini lavash + 🧀 cheese'),
        KeyboardButton('🌯 big lavash + 🧀 cheese'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

hot_dog_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('🌭 mini hot dog'), KeyboardButton('🌭 big hot dog'), KeyboardButton('🌭 ultra hot dog'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

taco_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('🌮 mini taco'), KeyboardButton('🌮 big taco'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

burger_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('🍔 mini burger'), KeyboardButton('🍔 big burger'), KeyboardButton('🍔 cheese burger'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

pizza_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('🍕 pipperoni pizza'), KeyboardButton('🍕 margarita pizza'), KeyboardButton('🍕 4 pizza'),
    ],
    [
        KeyboardButton('🍕 qazili pizza'), KeyboardButton('🍕 qo\'ziqorinli pizza')
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

steak_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('🥩 steak'), KeyboardButton('🥩steak + 🍟 kartoshka fri'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

muzqaymoq_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('🍨 muzqaymoq chocolate'), KeyboardButton('🍧 muzqaymoq vanilla'),
    ],
    [
        KeyboardButton('🍦 muzqaymoq milk')
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

tort_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('🎂 tort snickers'), KeyboardButton('🍰 tort napoleon'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

kartoshka_fri_keyboards = ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, keyboard=[
    [
        KeyboardButton('🍟 kartoshka fri'), KeyboardButton('🍟 kartoshka fri + 🥤 kola'),
    ],
    [
        KeyboardButton('🔙 Orqaga'),
    ]
])

