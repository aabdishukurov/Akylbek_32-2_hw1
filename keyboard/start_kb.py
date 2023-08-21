from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup
)

async def admin_select_users_keyboard():
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Список Пользователей",
        callback_data="admin_user_list"
    )
    markup.row(
        button_call_1,
    )
    return markup


async def new_start_keyboard():
    markup = InlineKeyboardMarkup()
    random_profiles_button = InlineKeyboardButton(
        "Просмотр анкетa",
        callback_data="random_profiles"
    )
    my_profile_button = InlineKeyboardButton(
        "Мой Профиль",
        callback_data="my_profile"
    )
    markup.row(
        random_profiles_button,
        my_profile_button
    )
    return markup

async def my_profile_detail_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    update_button = InlineKeyboardButton(
        "Изменить Анкету",
        callback_data="signup"
    )
    delete_button = InlineKeyboardButton(
        "Удаление Анкеты",
        callback_data="delete_profile"
    )
    markup.row(
        update_button,
        delete_button
    )
    return markup


async def if_not_profile_keyboard():
    markup = InlineKeyboardMarkup()
    signup_button = InlineKeyboardButton(
        "Регистрация",
        callback_data="signup"
    )
    markup.row(
        signup_button,
    )
    return markup