from telegram.loader import bot
from telebot.types import Message
from database.common.models import User, Ticket
from settings import Tg_settings


@bot.message_handler(func=lambda message: not message.is_topic_message)
def handle_user_message(message: Message) -> None:
    """
    Обработчик сообщений от пользователя.

    Пересылает их в тему форума, созданную ранее для этого пользователя

    :param message: Объект сообщения
    :return: None
    """
    tg_settings = Tg_settings()
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    user_id = message.from_user.id
    text = message.text
    if User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return
    ticket = Ticket.get_or_none(Ticket.user == user_id)
    chat = bot.get_chat(tg_settings.forum_id.get_secret_value())
    user_name = f"{first_name} {last_name}" if last_name else f"{first_name}"
    response_message = f"{user_name}: {text}"
    bot.send_message(chat.id, response_message, message_thread_id=ticket.ticket_id)
    bot.reply_to(message, "Сообщение отправлено!")
    return
