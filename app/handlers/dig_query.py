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
            await message.answer('<code>!dig yandex.ru</code>')
        elif len(msg) != 2:
            await message.answer(f'<code>!dig yandex.ru</code>')
        else:
            logging.info(pydig.query(msg[1]))
            await message.answer(f"<code>{pydig.query(msg[1], query_type='MX')}</code>")
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
