from aiogram import Bot
import os
from icecream import ic

bot_token = os.getenv('pt_hat_bot_token')
bot = Bot(token=bot_token, parse_mode="HTML")

admins = [539491282]

bot_commands = f'''
<code>!help</code> - Справка
<code>!menu</code> - Основное меню
<code>!id</code> - Показать ID
<code>!rev</code> - !rev 127.0.0.1 31337
<code>!links</code> - полезные ссылки
'''
