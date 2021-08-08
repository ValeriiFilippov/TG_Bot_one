from weather_api.weather_api import get_weather
from aiogram import types
from datastorage import sqlitestorage
from bot import dp


@dp.message_handlers(commands=["start"])
async def send_welcome(message: types.Message):
    await message.reply("Hi!\nI am weather bot!\n Enter your citi, please.")


@dp.message_handlers()
async def answer_weather(message: types.Message):
    info: str
    code: str
    info, code = await get_weather()
    kb = types.ReplyKeyboardMarkup([[types.KeyboardButton('Weather in my city')]], resize_keyboard=True)
    await message.answer(info, reply_markup=kb)

    if code != "404":
        sqlitestorage.write_data(message.from_user.id, message.text)


@dp.message_handlers()
async def answer_user_city_weather(message: types.Message):
    city = sqlitestorage.get_city(message.from_user.id)

    try:

        info, _ = await get_weather(city[0])
        await message.answer(info)
    except IndexError:
        await message.answer("Enter your city")
