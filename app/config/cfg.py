from aiogram import Bot
import os

bot_token = os.getenv('pt_hat_bot_token')
bot = Bot(token=bot_token, parse_mode="HTML")

all_commands = {'help_cmds': '!help', 'menu_cmds': '!menu', 'wiki_cmds': '!wiki',
                'id_cmds': '!id', 'cmds_cmds': '!cmds', 'rev_cmds': '!rev',
                'links_cmds': '!links',
                }

admins = [539491282]

bot_commands = f'''
🆘 <code>!help</code> - Справка
⚙️ <code>!menu</code> - Основное меню
ℹ️ <code>!id</code> - Показать ID
👁 <code>!rev</code> - Revshell
📑 <code>!links</code> - Полезные ссылки
📚 <code>!wiki</code> - Показать с вики
🎲 <code>!cmds</code> - Команды бота
'''
