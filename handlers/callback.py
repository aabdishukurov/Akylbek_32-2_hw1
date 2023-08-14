from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from aiogram import types, Dispatcher

from database.sql_commands import Database
from keyboards.start_kb import quiz_2_keyboard, quiz_1_keyboard


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


def register_callback_handlers(dp: Dispatcher):
    dp.register_message_handler(quiz_1, commands=['quiz'])
    dp.register_callback_query_handler(quiz_2, lambda call: call.data == "button_call_1")
    dp.register_callback_query_handler(answer_male, lambda call: call.data == "answer_male")
    dp.register_callback_query_handler(answer_female, lambda call: call.data == "answer_female")
    dp.register_callback_query_handler(admin_user_call, lambda call: call.data == "admin_user_list")