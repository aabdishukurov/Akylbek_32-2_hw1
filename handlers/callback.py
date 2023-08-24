import random
import re

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from aiogram import types, Dispatcher

from database.sql_commands import Database
from keyboards.start_kb import (
    quiz_2_keyboard,
    quiz_1_keyboard,
    like_dislike_keyboard,
    my_profile_detail_keyboard,
    if_not_profile_keyboard
)

async def quiz_1(message: types.Message):
    question = "Who invented Python"
    options = [
        "Voldemort",
        "Harry Potter",
        "Linus Torvalds",
        "Guido Van Rossum",
        "Witch"
    ]
    await bot.send_poll(
        chat_id=message.chat.id,
        question=question,
        options=options,
        is_anonymous=False,
        type='quiz',
        correct_option_id=3,
        reply_markup=await quiz_1_keyboard()
    )


async def quiz_2(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Male or Female ?",
        reply_markup=await quiz_2_keyboard()
    )


async def answer_male(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text='you are male'
    )


async def answer_female(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text='you are female'
    )


async def admin_user_call(call: types.CallbackQuery):
    users = Database().sql_admin_select_user_command()
    print(users)
    data = []
    for user in users:
        if not user["username"]:
            data.append(f"[{user['first_name']}](tg://user?id={user['telegram_id']})")
        else:
            data.append(f"[{user['username']}](tg://user?id={user['telegram_id']})")

    data = '\n'.join(data)
    await call.message.reply(text=data, parse_mode=types.ParseMode.MARKDOWN)


async def my_profile_call(call: types.CallbackQuery):
    user_form = Database().sql_select_user_form_by_telegram_id_command(
        telegram_id=call.from_user.id)
    print(user_form)
    try:
        with open(user_form[0]["photo"], 'rb') as photo:
            await bot.send_photo(
                chat_id=call.message.chat.id,
                photo=photo,
                caption=f"*Nickname:* {user_form[0]['nickname']}\n"
                        f"*Age:* {user_form[0]['age']}\n"
                        f"*Bio:* {user_form[0]['bio']}\n"
                        f"*Married:* {user_form[0]['married']}\n",
                parse_mode=types.ParseMode.MARKDOWN,
                reply_markup=await my_profile_detail_keyboard()
            )
    except IndexError as e:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="Вы не зарегистрированы можете нажать на кнопку и зарегистрироваться",
            reply_markup=await if_not_profile_keyboard()
        )


async def random_profiles_call(call: types.CallbackQuery):
    user_forms = Database().sql_select_user_forms_command()
    print(user_forms)
    random_form = random.choice(user_forms)
    print(random_form)
    with open(random_form["photo"], 'rb') as photo:
        await bot.send_photo(
            chat_id=call.message.chat.id,
            photo=photo,
            caption=f"*Nickname:* {random_form['nickname']}\n"
                    f"*Age:* {random_form['age']}\n"
                    f"*Bio:* {random_form['bio']}\n"
                    f"*Married:* {random_form['married']}\n",
            parse_mode=types.ParseMode.MARKDOWN,
            reply_markup=await like_dislike_keyboard(
                telegram_id=random_form["telegram_id"]
            )
        )


async def like_call(call: types.CallbackQuery):
    owner_telegram_id = re.sub("like_button_", "", call.data)
    is_like_existed = Database().sql_select_liked_form_command(
        owner_telegram_id=owner_telegram_id,
        liker_telegram_id=call.from_user.id
    )
    if is_like_existed:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text="Ты уже лайкал эту анкету"
        )
    else:
        Database().sql_insert_like_form_command(
            owner_telegram_id=owner_telegram_id,
            liker_telegram_id=call.from_user.id
        )
        await bot.send_message(
            chat_id=owner_telegram_id,
            text=f"Кому то понравилась твоя анкета \nМожешь перейти по ссылке и пообщаться [{call.from_user.first_name}](tg://user?id={call.from_user.id})",
            parse_mode=types.ParseMode.MARKDOWN_V2

        )
    await random_profiles_call(call=call)


async def delete_profile_call(call: types.CallbackQuery):
    Database().sql_delete_user_form(telegram_id=call.from_user.id)
    await bot.send_message(
        chat_id=call.message.chat.id,
        text="Deleted Successfully"
    )


def register_callback_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(answer_male, lambda call: call.data == "answer_male")
    dp.register_callback_query_handler(answer_female, lambda call: call.data == "answer_female")
    dp.register_callback_query_handler(admin_user_call, lambda call: call.data == "admin_user_list")
    dp.register_callback_query_handler(my_profile_call, lambda call: call.data == "my_profile")
    dp.register_callback_query_handler(random_profiles_call, lambda call: call.data == "random_profiles")
    dp.register_callback_query_handler(like_call, lambda call: "like_button_" in call.data)
    dp.register_callback_query_handler(delete_profile_call, lambda call: call.data == "delete_profile")