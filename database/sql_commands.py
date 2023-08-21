import sqlite3
from database import sql_queries
import random
import re
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import bot
from aiogram import types, Dispatcher




class Database:
    def __init__(self):
        self.connection = sqlite3.connect("db.sqlite3")
        self.cursor = self.connection.cursor()

    def sql_create_db(self):
        if self.connection:
            print("Database connected successfully")

        self.connection.execute(sql_queries.CREATE_USER_TABLE_QUERY)
        self.connection.commit()

    def sql_insert_user_command(self, telegram_id, username,
                                first_name, last_name):
        self.cursor.execute(sql_queries.START_INSERT_USER_QUERY,
                            (None,
                            telegram_id,
                            username,
                            first_name,
                            last_name)
                            )
        self.connection.commit()

    def sql_select_user_form_by_telegram_id_command(self, telegram_id):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "bio": row[4],
            "married": row[5],
            "photo": row[6]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_BY_TELEGRAM_ID_QUERY, (telegram_id,)
        ).fetchall()

    def sql_select_user_forms_command(self):
        self.cursor.row_factory = lambda cursor, row: {
            "id": row[0],
            "telegram_id": row[1],
            "nickname": row[2],
            "age": row[3],
            "bio": row[4],
            "married": row[5],
            "photo": row[6]
        }
        return self.cursor.execute(
            sql_queries.SELECT_USER_FORM_QUERY
        ).fetchall()



async def report_call(call: types.CallbackQuery):
    owner_telegram_id = re.sub( "", call.data)

    if owner_telegram_id in sql_queries.SELECT_USER_QUERY:
        is_report_existed = Database().sql_select_user_form_by_telegram_id_command(
        owner_telegram_id=owner_telegram_id,
        report_telegram_id=call.from_user.id
        )
        if is_report_existed:
            await bot.send_message(
                chat_id=call.message.chat.id,
                text="Ты уже жаловался на этого пользователя"
        )
        else:
            await bot.send_message(
                chat_id=owner_telegram_id,
                text=f"На вас пожаловался другой пользователь, и теперь вы находитесь в учёте",
                parse_mode=types.ParseMode.MARKDOWN_V2

            )
        await random_profiles_call(call=call)



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
            reply_markup=await report_keyboard(
                telegram_id=random_form["telegram_id"]
            ))