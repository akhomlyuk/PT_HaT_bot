from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import whois

router: Router = Router()


def whois_inf(host: str):
    try:
        domain = whois.query(host)
        return domain
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)


@router.message(F.text.startswith(cfg.all_commands['whois_cmds']))
async def whois_info(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer('<code>!whois yandex.ru</code>')
        elif len(msg) != 2:
            await message.answer(f'<code>!whois yandex.ru</code>')
        else:
            ic(whois_inf(msg[1]))
            await message.answer(f"{whois_inf(msg[1])}")
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
