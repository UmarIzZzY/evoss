from aiogram import types
from aiogram.dispatcher.filters import Text, Command
from keyboards.default.menu_kb import menu_keyboards
from loader import dp


@dp.message_handler(Text(equals="🍴 Menu"))
@dp.message_handler(lambda message: message.text == "🍴 Menu")
async def menu(message: types.Message):
    await message.answer("Menu bo'limi", reply_markup=menu_keyboards)


from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text
from keyboards.default.menu_kb import menu_keyboards
from keyboards.inline.buy_kb import buy_product_new
from loader import dp


@dp.message_handler(Text(equals="🍴 Menu"))
async def menu(message: types.Message):
    await message.answer("Menu bo'limi", reply_markup=menu_keyboards)


@dp.message_handler(text="🌯 Lavash")
async def lavash_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🌯 Lavash")
    lavash_rasm = "https://cp.ectn.uz/files//0622/lavash_s_govyadinoy_evos.png"
    info = (
        "Narxi: 28000 so'm\nShirali gril mol go'shti va yetilib pishgan pomidor bo'lakchalari, tillarang kartoshka chipslari"
        ", yangi, klassik lavashdagi barra piyoz va ko'katlar bilan sharqona tomat sousi")
    await message.answer_photo(photo=lavash_rasm, caption=info, reply_markup=buy_product_new)


@dp.message_handler(text="🌭 Hot dog")
async def hotdog_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🌭 Hot dog")
    rasm = "https://cp.ectn.uz/files//0622/hot_dog_Baguette_evos.png"
    info = (
        "Narxi: 28000 so'm\nShirali gril mol go'shti va yetilib pishgan pomidor bo'lakchalari, tillarang kartoshka chipslari"
        ", yangi, klassik lavashdagi barra piyoz va ko'katlar bilan sharqona tomat sousi")
    await message.answer_photo(photo=rasm, caption=info, reply_markup=buy_product_new)


@dp.message_handler(text="🍔 Burger")
async def burger_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🍔 Burger")
    rasm = "https://avatars.mds.yandex.net/get-sprav-products/9495815/2a0000018a742bb0bf1e212eacefb8c0b696/orig"
    info = (
        "Narxi: 28000 so'm\nShirali gril mol go'shti va yetilib pishgan pomidor bo'lakchalari, tillarang kartoshka chipslari"
        ", yangi, klassik lavashdagi barra piyoz va ko'katlar bilan sharqona tomat sousi")
    await message.answer_photo(photo=rasm, caption=info, reply_markup=buy_product_new)


@dp.message_handler(text="🥩 Steyk")
async def steyk_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🥩 Steyk")
    rasm = "https://avatars.mds.yandex.net/i?id=4f7be101bc0ffcd133a570d53806273365cd6929-9705291-images-thumbs&n=13"
    info = (
        "Narxi: 28000 so'm\nShirali gril mol go'shti va yetilib pishgan pomidor bo'lakchalari, tillarang kartoshka chipslari"
        ", yangi, klassik lavashdagi barra piyoz va ko'katlar bilan sharqona tomat sousi")
    await message.answer_photo(photo=rasm, caption=info, reply_markup=buy_product_new)


@dp.message_handler(text="🍕 Pizza")
async def pizza_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🍕 Pizza")
    rasm = "https://avatars.mds.yandex.net/i?id=1261ca8206fd2aaa7ef07d58a565e19e2c3f6864-10877308-images-thumbs&n=13"
    info = (
        "Narxi: 28000 so'm\nShirali gril mol go'shti va yetilib pishgan pomidor bo'lakchalari, tillarang kartoshka chipslari"
        ", yangi, klassik lavashdagi barra piyoz va ko'katlar bilan sharqona tomat sousi")
    await message.answer_photo(photo=rasm, caption=info, reply_markup=buy_product_new)


@dp.message_handler(text="🍕 Pizza")
async def pizza_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🍕 Pizza")
    rasm = "https://avatars.mds.yandex.net/i?id=1261ca8206fd2aaa7ef07d58a565e19e2c3f6864-10877308-images-thumbs&n=13"
    info = (
        "Narxi: 28000 so'm\nShirali gril mol go'shti va yetilib pishgan pomidor bo'lakchalari, tillarang kartoshka chipslari"
        ", yangi, klassik lavashdagi barra piyoz va ko'katlar bilan sharqona tomat sousi")
    await message.answer_photo(photo=rasm, caption=info, reply_markup=buy_product_new)


@dp.message_handler(text="🌮 Taco")
async def taco_handler(message: types.Message, state: FSMContext):
    await state.update_data(product_name="🌮 Taco")
    rasm = ""
    info = (
        "Narxi: 28000 so'm\nShirali gril mol go'shti va yetilib pishgan pomidor bo'lakchalari, tillarang kartoshka chipslari"
        ", yangi, klassik lavashdagi barra piyoz va ko'katlar bilan sharqona tomat sousi")
    await message.answer_photo(photo=rasm, caption=info, reply_markup=buy_product_new)


@dp.callback_query_handler(text="buy_product_new")
async def buy_product_new_handler(call: types.CallbackQuery, state: FSMContext):
    data = await state.get_data()
    product_name = data.get("product_name")
    text = f"Sotib olindi, {product_name}"
    await call.message.answer(text=text)
