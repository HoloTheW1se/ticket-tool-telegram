from datetime import datetime
from telebot.apihelper import create_forum_topic
from telebot.types import Message
from settings import Tg_settings
from telegram.loader import bot
from peewee import IntegrityError
from database.common.models import db, User, Ticket
from telegram.utils.get_topic_id import get_topic_id


@bot.message_handler(commands=["start"])
def handle_start(message: Message) -> None:
    tg_settings = Tg_settings()
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name
    last_name = message.from_user.last_name
    try:
        with db:
            user = User.create(user_id=user_id, username=username, first_name=first_name, last_name=last_name)
            forum_id = tg_settings.forum_id.get_secret_value()
            topic_name = f"{user_id}-{datetime.now()}"
            create_forum_topic(forum_id, topic_name)
            topic_id, is_found = get_topic_id(bot, user_id, forum_id)

            if is_found:
                Ticket.create(user=user, chat_id=topic_id)
            else:
                bot.reply_to(message, "Возникла ошибка! Тикет не был создан.")
        bot.reply_to(message, f"Добро пожаловать, {first_name}!\n"
                              f"Заполните форму, чтобы администрация могла помочь вам!\n"
                              f"1. Игра\n"
                              f"2. Игровой ник\n"
                              f"3. Название трайба\n"
                              f"4. Стим ник или id\n"
                              f"5. Причина обращения\n"
                              f"6. Уточнить карту; указать координаты через ccc"
                     )

    except IntegrityError:
        bot.reply_to(message, f"Рад Вас снова видеть, {first_name}!\n"
                              f"Заполните форму, чтобы администрация могла помочь вам!\n"
                              f"1. Игра\n"
                              f"2. Игровой ник\n"
                              f"3. Название трайба\n"
                              f"4. Стим ник или id\n"
                              f"5. Причина обращения\n"
                              f"6. Уточнить карту; указать координаты через ccc"
                     )
    return
