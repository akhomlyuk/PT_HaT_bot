from aiogram import Bot
import os

bot_token = os.getenv('pt_hat_bot_token')
bot = Bot(token=bot_token, parse_mode="HTML")

all_commands = {'help_cmds': '!help', 'menu_cmds': '!menu', 'wiki_cmds': '!wiki', 'dig_cmds': '!dig', 'commands_cmds': '!commands',
                'id_cmds': '!id', 'jwt_cmds': '!jwt', 'cmds_cmds': '!cmds', 'rev_cmds': '!rev', 'sqli_cmds': '!sqli',
                'search_sploit_cmds': '!ss', 'checkport_cmds': '!port', 'whois_cmds': '!whois', 'uncurl_cmds': '!uncurl',
                'hash_alz_cmds': '!hash', 'b64decode_cmds': '!b64d', 'b64encode_cmds': '!b64e', 'hex2text_cmds': '!h2t',
                'text2hex_cmds': '!t2h', 'gpt_cmds': '!gpt', 'links_cmds': '!links', 'ssti_cmds': '!ssti'
                }

admins = [539491282]

bot_commands = f'''
🆘 <code>!help</code> - Справка
⚙️ <code>!menu</code> - Основное меню
ℹ️ <code>!id</code> - Показать ID
🔮 <code>!hash</code> - Определить хеш
🔋 <code>!jwt</code> - Декодер JWT
🔎 <code>!whois</code> - Whois домена
👁 <code>!rev</code> - Revshell
🧨 <code>!ss</code> - Search Sploit
💉 <code>!sqli</code> - SQLi payloads
🔍 <code>!port</code> - Проверить порт
📄 <code>!dig</code> - Просмотр DNS записей
🖌 <code>!b64e</code> <code>!b64d</code> - base64
🤖 <code>!gpt</code> - Список ChatGPT
📑 <code>!links</code> - Полезные ссылки
📚 <code>!wiki</code> - Показать с вики
🎲 <code>!cmds</code> - Команды бота
'''
