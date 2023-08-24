import random
import re

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from aiogram import types, Dispatcher
from aiogram.utils.deep_linking import _create_link

from const import REFERENCE_MENU_TEXT, REFERENCE_LINK_TEXT
from database.sql_commands import Database
import binascii
import os

from keyboards.reference_keyboard import reference_menu_keyboard


async def reference_menu_call(call: types.CallbackQuery):
    await bot.send_message(
        chat_id=call.message.chat.id,
        text=REFERENCE_MENU_TEXT,
        reply_markup=await reference_menu_keyboard(),
        parse_mode=types.ParseMode.MARKDOWN
    )


async def reference_link_call(call: types.CallbackQuery):
    is_link_existed = Database().sql_select_user_link_command(
        telegram_id=call.from_user.id
    )
    print(is_link_existed)
    if is_link_existed[0]['link'] is None:
        token = binascii.hexlify(os.urandom(4)).decode()
        link = await _create_link(link_type="start", payload=token)
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=REFERENCE_LINK_TEXT.format(
                link=link
            ),
        )
        Database().sql_update_user_by_link(
            link=link,
            telegram_id=call.from_user.id
        )
    else:
        await bot.send_message(
            chat_id=call.message.chat.id,
            text=REFERENCE_LINK_TEXT.format(
                link=is_link_existed[0]['link']
            ),
        )


async def reference_list_call(call: types.CallbackQuery):
    users = Database().sql_select_all_reference_command(
        owner_telegram_id=call.from_user.id
    )
    print(users)
    if users:
        data = []
        for user in users:
            data.append(f"[{user['id']}](tg://user?id={user['id']})")

        data = '\n'.join(data)
        await call.message.reply(text=data, parse_mode=types.ParseMode.MARKDOWN)
    else:
        await call.message.reply(text='У вас нету рефералов', parse_mode=types.ParseMode.MARKDOWN)


def register_reference_handlers(dp: Dispatcher):
    dp.register_callback_query_handler(reference_menu_call,
                                       lambda call: call.data == "reference_menu")
    dp.register_callback_query_handler(reference_link_call,
                                       lambda call: call.data == "reference_link")
    dp.register_callback_query_handler(reference_list_call,
                                       lambda call: call.data == "referral_list")