from aiogram.dispatcher.filters.state import StatesGroup, State


class RegisterState(StatesGroup):
    full_name = State()
    age = State()
    phone_number = State()
    user_id = State()
