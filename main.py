from aiogram.utils import executor
from config import dp
from handlers import (
    start,
    callback,
    chat_actions,
    fsm_form,
    reference
)
from database import sql_commands


async def onstart_up(_):
    db = sql_commands.Database()
    db.sql_create_db()


start.register_start_handlers(dp)
callback.register_callback_handlers(dp)
reference.register_reference_handlers(dp)
fsm_form.register_fsm_form_handlers(dp)
chat_actions.register_chat_actions_handlers(dp)

if __name__ == "__main__":
    executor.start_polling(dp,
                           skip_updates=True,
                           on_startup=onstart_up)