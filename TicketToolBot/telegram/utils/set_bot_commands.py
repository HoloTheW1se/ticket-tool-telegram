from telebot.types import BotCommand
from settings import default_commands


def set_default_commands(bot):
    """
    Устанавливает стандартные команды бота, чтобы предлагать пользователю

    :param bot: Объект бота
    :return: None
    """
    bot.set_my_commands(
        [BotCommand(*command) for command in default_commands]
    )
