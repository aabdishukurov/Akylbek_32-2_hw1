from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup
)


async def select_my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    my_profile_button = InlineKeyboardButton(
        "Мой Профиль",
        callback_data="my_profile"
    )
    markup.add(
        my_profile_button,
    )
    return markup