from telegram.loader import bot
import telegram.handlers
from database.common.models import db, Base_model
from telegram.utils.set_bot_commands import set_default_commands

if __name__ == "__main__":
    db.connect()
    db.create_tables(Base_model.__subclasses__())
    set_default_commands(bot)
    bot.infinity_polling()
