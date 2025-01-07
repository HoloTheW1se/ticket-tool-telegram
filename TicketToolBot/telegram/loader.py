from settings import Tg_settings
from telebot import TeleBot

tg_settings = Tg_settings()
bot = TeleBot(tg_settings.bot_token.get_secret_value())
