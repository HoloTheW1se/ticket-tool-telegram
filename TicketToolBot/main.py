from telegram_api.loader import bot
import telegram_api.handlers
from telegram_api.utils.set_bot_commands import set_default_commands

if __name__ == "__main__":
    set_default_commands(bot)
    bot.infinity_polling()
