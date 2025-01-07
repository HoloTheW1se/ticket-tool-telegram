import os
from dotenv import load_dotenv
from pydantic import SecretStr, StrictStr
from pydantic_settings import BaseSettings

load_dotenv()

db_path = 'database.db'


class Tg_settings(BaseSettings):
    bot_token: SecretStr = os.getenv('bot_token', None)
    forum_id: SecretStr = os.getenv('forum_id', None)


default_commands = (
    ("start", "Запустить бота"),
    ("help", "Вывести справку"),
)
