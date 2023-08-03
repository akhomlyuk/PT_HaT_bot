from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic

router: Router = Router()


def hex_to_text(text: str):
    if text[:2] == '0x':
        text = text[2:]
    plain_text = bytes.fromhex(text).decode('utf-8')
    return plain_text


def text_to_hex(text: str):
    text = text.encode('utf-8')
    return text.hex()


@router.message(F.text.startswith(cfg.all_commands['hex2text_cmds']))
async def send_hex2text_string(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer(f'Пример:\n<code>!h2t 50656e74657374204861636b7320616e6420546f6f6c73</code>')
        elif len(msg) > 2:
            await message.answer(
                f'Неправильная hex последовательность\nПример:\n<code>!h2t 50656e74657374204861636b7320616e6420546f6f6c73</code>')
        else:
            msg2 = message.text[5:]
            await message.answer(f'<code>{hex_to_text(msg2)}</code>')
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()


@router.message(F.text.startswith(cfg.all_commands['text2hex_cmds']))
async def send_text2hex_string(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer(f'Пример:\n<code>!t2h Pentest Hacks and Tools</code>')
        else:
            msg2 = message.text[5:]
            await message.answer(f'<code>{text_to_hex(msg2)}</code>')
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
