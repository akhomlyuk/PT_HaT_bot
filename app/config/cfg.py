from aiogram import Bot
import os
from icecream import ic

bot_token = os.getenv('pt_hat_bot_token')
bot = Bot(token=bot_token, parse_mode="HTML")

admins = [539491282]
