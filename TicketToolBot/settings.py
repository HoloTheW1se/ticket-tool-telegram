import os
from dotenv import load_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

# Загрузка .env-файла
load_dotenv()

# Название файла с БД
db_path = 'database.db'


class Tg_settings(BaseSettings):
    """
    Класс для защищенной передачи токена и айди форума.
    """
    bot_token: SecretStr = os.getenv('bot_token', None)
    forum_id: SecretStr = os.getenv('forum_id', None)


# Стандартные команды для предложения пользователю
default_commands = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
)
