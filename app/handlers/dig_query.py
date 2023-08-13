from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import pydig

router: Router = Router()

resolver = pydig.Resolver(executable='/usr/bin/dig', nameservers=['1.1.1.1', '1.0.0.1'], additional_args=['+time=10'])


@router.message(F.text.startswith(cfg.all_commands['dig_cmds']))
async def dig_query(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer('<code>!dig ya.ru (A,MX,TXT,etc)</code>\n\nhttps://en.wikipedia.org/wiki/List_of_DNS_record_types', disable_web_page_preview=True)
        elif len(msg) != 3:
            await message.answer('<code>!dig ya.ru (A,MX,TXT,etc)</code>\n\nhttps://en.wikipedia.org/wiki/List_of_DNS_record_types', disable_web_page_preview=True)
        else:
            query = pydig.query(msg[1], msg[2])
            await message.answer(f"<code>{query}</code>")
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
