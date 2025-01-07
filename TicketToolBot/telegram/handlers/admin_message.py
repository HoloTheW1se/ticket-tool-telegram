from telebot.types import Message
from telegram.loader import bot
from database.common.models import Ticket


@bot.message_handler(func=lambda message: message.is_topic_message)
def handle_answer(message: Message) -> None:
    """
    Обработчик сообщений в тикетах.

    Ищет пользователя, создавшего топик.
    Отправляет пользователю сообщение, написанное в тикете

    :param message: Объект сообщения
    :return: None
    """
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    text = message.text

    topic_id = message.message_thread_id

    ticket = Ticket.get_or_none(Ticket.ticket_id == topic_id)
    chat_id = ticket.chat_id

    admin_name = f"{first_name} {last_name}" if last_name else f"{first_name}"
    response_message = f"{admin_name}: {text}"

    bot.send_message(chat_id, response_message)
    return
