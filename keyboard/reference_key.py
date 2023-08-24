from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup
)


async def reference_menu_keyboard():
    markup = InlineKeyboardMarkup()
    link_button = InlineKeyboardButton(
        "Реферальная ссылка 🔗",
        callback_data="reference_link"
    )
    balance_button = InlineKeyboardButton(
        "Список Рефералов 💵",
        callback_data="referral_list"
    )
    markup.add(
        link_button,
    ).add(
        balance_button
    )
    return markup