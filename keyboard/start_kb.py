from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton,
    KeyboardButton,
    ReplyKeyboardMarkup
)


async def start_keyboard():
    quiz_button = KeyboardButton("/quiz")
    mark_up = ReplyKeyboardMarkup(
        one_time_keyboard=True,
        resize_keyboard=True
    )
    mark_up.add(quiz_button)
    return mark_up


async def quiz_1_keyboard():
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Следующая Викторина",
        callback_data="button_call_1"
    )
    markup.add(button_call_1)
    return markup


async def quiz_2_keyboard():
    markup = InlineKeyboardMarkup()
    button_call_1 = InlineKeyboardButton(
        "Male",
        callback_data="answer_male"
    )
    button_call_2 = InlineKeyboardButton(
        "Female",
        callback_data="answer_female"
    )
    markup.row(
        button_call_1,
        button_call_2
    )
    return markup


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
        "Просмотр анкет 🎉",
        callback_data="random_profiles"
    )
    my_profile_button = InlineKeyboardButton(
        "Мой Профиль",
        callback_data="my_profile"
    )
    referral_button = InlineKeyboardButton(
        "Реферальная программа",
        callback_data="reference_menu"
    )
    markup.add(
        random_profiles_button
    ).add(
        my_profile_button
    ).add(
        referral_button
    )
    return markup


async def like_dislike_keyboard(telegram_id):
    markup = InlineKeyboardMarkup(row_width=2)
    like_button = InlineKeyboardButton(
        "👍🏻",
        callback_data=f"like_button_{telegram_id}"
    )
    dislike_button = InlineKeyboardButton(
        "👎🏻",
        callback_data="random_profiles"
    )
    markup.row(
        like_button,
        dislike_button
    )
    return markup


async def my_profile_detail_keyboard():
    markup = InlineKeyboardMarkup(row_width=2)
    update_button = InlineKeyboardButton(
        "Изменить Анкету 💡",
        callback_data="signup"
    )
    delete_button = InlineKeyboardButton(
        "Удаление Анкеты ❌",
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
        "Регистрация 💡",
        callback_data="signup"
    )
    markup.row(
        signup_button,
    )
    return markup