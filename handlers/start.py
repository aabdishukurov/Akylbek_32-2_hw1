import sqlite3
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from aiogram import types, Dispatcher
from database import sql_commands


async def start_button(message: types.Message):
    sql_commands.Database().sql_insert_user_command(
        telegram_id=message.from_user.id,
        username=message.from_user.username,
        first_name=message.from_user.first_name,
        last_name=message.from_user.last_name,
    )

    print(message)

    # await message.reply(f"Hello {message.from_user.username}")
    await bot.send_message(
        chat_id=message.from_user.id,
        text=f'Hello {message.from_user.username}\n'
             f'https://youtube.com'
    )


def register_start_handlers(dp: Dispatcher):
    dp.register_message_handler(start_button, commands=['start'])
