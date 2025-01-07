from telegram.loader import bot
from telebot.types import Message
from telebot import types
from database.common.models import User, Ticket


@bot.message_handler(func=lambda message: True)
def handle_user_message(message: Message) -> None:
    username = message.from_user.username
    user_id = message.from_user.id
    message = message.text
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return

    ticket = Ticket.get_or_none(Ticket.user.id == user_id)
    message = f"{username}: {message}"
    bot.send_message(ticket.chat_id, message)
    return
