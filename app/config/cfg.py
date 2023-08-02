from aiogram import Bot
import os

bot_token = os.getenv('pt_hat_bot_token')
bot = Bot(token=bot_token, parse_mode="HTML")

admins = [539491282]

bot_commands = f'''
<code>!help</code> - Справка
<code>!menu</code> - Основное меню
<code>!id</code> - Показать ID
<code>!rev</code> - <code>!rev 127.0.0.1 31337</code>
<code>!rev bash 127.0.0.1 31337</code>
<code>!links</code> - Полезные ссылки
'''
