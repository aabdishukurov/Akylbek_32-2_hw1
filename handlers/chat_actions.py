import datetime
from config import bot
from aiogram import types, Dispatcher

async def ban_sys(message: types.Message):
    ban_words = ["badass", "damn", "shit", "fuck", "munter", "bitch"]
    if message.chat.id == -1001940767325:
        for word in ban_words:
            if word in message.text.lower().replace(" ", ""):
                await bot.delete_message(
                    chat_id=message.chat.id,
                    message_id=message.message_id
                )
                await bot.send_message(
                    chat_id=message.chat.id,
                    text=f"Предупреждение: ещё одно ненормативное сообщение и вы получите блокировку\n\n"
                         f'Пользователь {message.from_user.username}'
                )


def register_chat_actions_handlers(dp: Dispatcher):
    dp.register_message_handler(ban_sys)