from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from app.helpers.sqli_gen import get_sqli_tables, get_sqli_columns, get_sqli_data
from app.texts.sqli_examples import sqli_example
from icecream import ic

router: Router = Router()


@router.message(F.text.startswith(cfg.all_commands['sqli_cmds']))
async def send_sqli_payload(message: Message):
    try:
        payload = message.text.split(' ')
        if len(payload) == 1:
            await message.answer(sqli_example)
        elif len(payload) == 2:
            await message.answer(f'<code>{get_sqli_tables(payload[1])[0]}</code>\n\n<code>{get_sqli_tables(payload[1])[1]}</code>'
                                 f'\n\nMore info: https://book.hacktricks.xyz/pentesting-web/sql-injection')
        elif len(payload) == 3:
            await message.answer(f'<code>{get_sqli_columns(payload[2])[0]}</code>\n\n<code>{get_sqli_columns(payload[2])[1]}</code>'
                                 f'\n\nMore info: https://book.hacktricks.xyz/pentesting-web/sql-injection')
        elif len(payload) == 4:
            data = ' '.join(payload)
            await message.answer(f'<code>{get_sqli_data(data)[0]}</code>\n\n<code>{get_sqli_data(data)[1]}</code>'
                                 f'\n\nMore info: https://book.hacktricks.xyz/pentesting-web/sql-injection')
        else:
            await message.answer(sqli_example)
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
