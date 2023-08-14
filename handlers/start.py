from config import bot
from aiogram import types, Dispatcher

from const import START_MENU_TEXT
from database import sql_commands
from keyboards.start_kb import admin_select_users_keyboard, start_keyboard


async def start_button(message: types.Message):
    sql_commands.Database().sql_insert_user_command(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    print(message)
    # with open("/Users/adiletsaparbek/PycharmProjects/geek_32_2/media/menu_photo.jpg", "rb") as photo:
    #     await bot.send_photo(
    #         chat_id=message.chat.id,
    #         photo=photo,
    #         caption=START_MENU_TEXT.format(
    #             user=message.from_user.username
    #         ),
    #         parse_mode=types.ParseMode.MARKDOWN
    #     )

    with open("/Users/adiletsaparbek/PycharmProjects/geek_32_2/media/dostbot_animation.gif", "rb") as animation:
        await bot.send_animation(
            chat_id=message.chat.id,
            animation=animation,
            caption=START_MENU_TEXT.format(
                user=message.from_user.username
            ),
            parse_mode=types.ParseMode.MARKDOWN,
            reply_markup=await start_keyboard()
        )


async def secret_word(message: types.Message):
    if message.from_user.id == 1150258083:
        await bot.delete_message(
            chat_id=message.chat.id,
            message_id=message.message_id
        )
        await bot.send_message(
            chat_id=message.from_user.id,
            text="Yes, my master",
            reply_markup=await admin_select_users_keyboard()
        )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
    dp.register_message_handler(secret_word, lambda word: 'dorei' in word.text)