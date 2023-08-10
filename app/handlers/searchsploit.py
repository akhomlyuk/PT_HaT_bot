from aiogram import Router, F, html
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import os

router: Router = Router()


@router.message(F.text.in_('!ss'))
async def search_sploit(message: Message):
    try:
        msg = message.text.split()
        sploit_string = ' '.join(msg[1])
        ss = os.popen(f'searchsploit {sploit_string} -j -w').read()[:-1]
        await message.answer(f'{ss}')
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
