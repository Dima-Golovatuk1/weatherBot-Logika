from aiogram.types import KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboardMarkup

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Погода'), KeyboardButton(text='Про нас')],
        [KeyboardButton(text='Контакти')]
    ],
    resize_keyboard=True,
    input_field_placeholder='Обери пункт меню нижче'
    )

country_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Німеччина', callback_data='country_Germany'),
            InlineKeyboardButton(text='Україна', callback_data='country_Ukraine')
        ],
        [

        ]
    ]
)

ukraine_inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Обухів', callback_data='weather_Obukhiv'),
            InlineKeyboardButton(text='Одеса', callback_data='weather_Odesa')
        ]
    ]
)

germany_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Київ', callback_data='weather_Kyiv'),
        ]
    ]
)