from telegram.loader import bot
from telebot.types import Message
from database.common.models import User, Ticket
from settings import Tg_settings


@bot.message_handler(content_types=['video'])
def handle_video(message: Message):
    tg_settings = Tg_settings()
    user_id = message.from_user.id
    file_id = message.video.file_id
    if message.is_topic_message:
        topic_id = message.message_thread_id
        ticket = Ticket.get_or_none(Ticket.ticket_id == topic_id)
        chat_id = ticket.chat_id
        bot.send_video(chat_id, file_id)
    elif User.get_or_none(User.user_id == user_id) is None:
        bot.reply_to(message, "Вы не зарегистрированы. Напишите /start")
        return
    else:
        ticket = Ticket.get_or_none(Ticket.user == user_id)
        chat = bot.get_chat(tg_settings.forum_id.get_secret_value())
        bot.send_video(chat.id, file_id, message_thread_id=ticket.ticket_id)
    bot.reply_to(message, "Видео отправлено!")
    return
