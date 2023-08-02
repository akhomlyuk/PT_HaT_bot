from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import base64

router: Router = Router()


def b64_decode(b64_enc: str):
    try:
        b64_dec = base64.b64decode(b64_enc.encode())
        return b64_dec.decode('utf-8')
    except Exception as e:
        ic(e)


def b64_encode(plain_text: str):
    try:
        b64_enc = base64.b64encode(plain_text.encode())
        return b64_enc.decode('utf-8')
    except Exception as e:
        ic(e)


@router.message(F.text.startswith(cfg.all_commands['b64decode_cmds']))
async def send_b64_decode(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer(f'Пример:\n<code>!b64_decode UGVudGVzdCBIYVQ=</code>')
        else:
            await message.answer(f'{b64_decode(msg[1])}')
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()


@router.message(F.text.startswith(cfg.all_commands['b64encode_cmds']))
async def send_b64_encode(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer(f'Пример:\n<code>!b64_encode Pentest HaT</code>')
        else:
            msg2 = message.text[12:]
            await message.answer(f'{b64_encode(msg2)}')
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
