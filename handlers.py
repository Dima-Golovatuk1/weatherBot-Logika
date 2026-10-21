from aiogram import F, Router, html, types
from aiogram.types import Message, CallbackQuery
from aiogram.filters import Command, CommandStart

from keyboards import main_keyboard, country_keyboard, ukraine_inline_keyboard, germany_keyboard
from services import get_weather, ask_gemini

router = Router()

@router.message(CommandStart())
async def start(message: types.Message):
    user_name = html.quote(message.from_user.first_name)
    await message.answer(f'Привіт: {user_name}',
                         reply_markup = main_keyboard)

# @router.message(F.text == 'Погода')
# async def weather(message: types.Message):
#     weather_report = get_weather()
#
#     if (weather_report['code'] == 200):
#         weather_text = (
#             f'Погода в місті {weather_report['city']}: \n'
#             f'Температура: {weather_report['current_temp']} \n'
#             f'Швидкість вітру: {weather_report['wind_speed']} \n'
#             f'Вологість: {weather_report['humidity']}% \n'
#         )
#     else :
#         weather_text = weather_report['error']
#
#     await message.answer(weather_text)

@router.message(F.text == 'Погода')
async def city_menu(message: types.Message):
    await message.answer(
        'Оберіть країну, для якого хочеш дізнатися погоду',
        reply_markup = country_keyboard
    )

@router.callback_query(F.data.startswith('country_'))
async def city_callback(callback: CallbackQuery):
    country = callback.data.split('_')[1]
    btn = ukraine_inline_keyboard

    if country == 'Ukraine':
        btn = ukraine_inline_keyboard
    elif country == 'Germany':
        btn = germany_keyboard

    await callback.message.edit_text(
        text='Оберіть місто, для якого хочеш дізнатися погоду',
        reply_markup=btn
    )

    await callback.answer()



@router.callback_query(F.data.startswith('weather_'))
async def weather_callback(callback: CallbackQuery):
    city = callback.data.split('_')[1]
    weather_report = get_weather(city)

    if (weather_report['code'] == 200):
        weather_text = (
            f'Погода в місті {weather_report['city']}: \n'
            f'Температура: {weather_report['current_temp']} \n'
            f'Швидкість вітру: {weather_report['wind_speed']} \n'
            f'Вологість: {weather_report['humidity']}% \n'
        )
    else :
        weather_text = weather_report['error']

    await callback.message.edit_text(
        text=weather_text,
        reply_markup=ukraine_inline_keyboard
    )

    await callback.answer()

@router.message(F.text == 'Про нас')
async def weather(message: types.Message):
    await message.answer('Я там такий то крутий розробник')


@router.message(F.text == 'Контакти')
async def weather(message: types.Message):
    await message.answer('номер телефону: +0980492653')

@router.message(Command('ask'))
async def gemini_handlers(message: types.Message):
    user_prompt = message.text.replace('/ask', '').strip()

    if not user_prompt:
        await message.answer('Будь ласка напишіть своє питання після команди /ask')
        return

    wait_message = await message.answer('Думаю над відповідю...')

    ai_response = ask_gemini(user_prompt)
    await wait_message.edit_text(ai_response)

@router.message()
async def weather_in_city(message: types.Message):
    city = message.text
    weather_report = get_weather(city)

    wait_message = await message.answer('Думаю над відповідю...')

    if (weather_report['code'] == 200):
        weather_text = (
            f'Погода в місті {weather_report['city']}: \n'
            f'Температура: {weather_report['current_temp']} \n'
            f'Швидкість вітру: {weather_report['wind_speed']} \n'
            f'Вологість: {weather_report['humidity']}% \n'
        )

        ai_response = ask_gemini(weather_text)

    else :
        ai_response = weather_report['error']

    await wait_message.edit_text(ai_response)

# @router.message()
# async def echo(message: types.Message):
#     num = int(message.text)
#
#     if num <= -300:
#         await message.answer(f"Де ти взяв таку температуру?")
#     elif num > 60:
#         await message.answer(f'Де ти взяв таку температуру?')
#     elif num > 300 and num < 0:
#         await message.answer(f"Тобі слід одягнутися")
#     elif num >= 0 and num <=15:
#         await message.answer(f'Тобі слід легко одягнутися')
#     else:
#         await message.answer(f'Ой як жарко')
