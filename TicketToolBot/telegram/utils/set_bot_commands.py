from telebot.types import BotCommand
from settings import default_commands


def set_default_commands(bot):
    bot.set_my_commands(
        [BotCommand(*command) for command in default_commands]
    )
