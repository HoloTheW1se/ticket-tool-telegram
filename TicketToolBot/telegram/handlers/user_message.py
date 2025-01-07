from telegram.loader import bot
from telebot.types import Message
from telebot import types
from database.common.models import User, Ticket
from settings import Tg_settings


@bot.message_handler(func=lambda message: True)
def handle_user_message(message: Message) -> None:
    """
    Обработчик сообщений от пользователя.

    Пересылает их в тему форума, созданную ранее для этого пользователя

    :param message: Объект сообщения
    :return: None
    """
    tg_settings = Tg_settings()
    username = message.from_user.username
    user_id = message.from_user.id
    text = message.text
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return
    ticket = Ticket.get_or_none(Ticket.user == user_id)
    chat = bot.get_chat(tg_settings.forum_id.get_secret_value())
    text = f"{username}: {text}"
    bot.send_message(chat.id, text, message_thread_id=ticket.chat_id)
    return
