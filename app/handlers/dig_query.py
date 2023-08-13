from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import pydig

router: Router = Router()


@router.message(F.text.startswith(cfg.all_commands['dig_cmds']))
async def dig_query(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer('<code>!dig ya.ru</code>\nor\n<code>!dig ya.ru (A,MX,TXT,etc)</code>\n\nhttps://en.wikipedia.org/wiki/List_of_DNS_record_types', disable_web_page_preview=True)
        elif len(msg) == 2:
            query_a = pydig.query(msg[1], 'A')
            query_cname = pydig.query(msg[1], 'CNAME')
            query_mx = pydig.query(msg[1], 'MX')
            query_ns = pydig.query(msg[1], 'NS')
            query_ptr = pydig.query(msg[1], 'PTR')
            query_soa = pydig.query(msg[1], 'SOA')
            query_txt = pydig.query(msg[1], 'TXT')
            await message.answer(f"<b>A</b>: <code>{query_a}</code>\n<b>CNAME</b>: <code>{query_cname}</code>\n<b>MX</b>: <code>{query_mx}</code>\n<b>NS</b>: <code>{query_ns}</code>"
                                 f"\n<b>PTR</b>: <code>{query_ptr}</code>\n<b>SOA</b>: <code>{query_soa}</code>\n<b>TXT</b>: <code>{query_txt}</code>")
        elif len(msg) != 3:
            await message.answer('<code>!dig ya.ru</code>\nor\n<code>!dig ya.ru (A,MX,TXT,etc)</code>\n\nhttps://en.wikipedia.org/wiki/List_of_DNS_record_types', disable_web_page_preview=True)
        else:
            query = pydig.query(msg[1], msg[2])
            await message.answer(f"<code>{query}</code>")
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
