import requests
from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
import json

router: Router = Router()


def check_hash_string(hash_string: str):
    try:
        headers = {'Content-Type': 'application/json'}
        url = requests.get(f'https://weakpass.com/api/v1/search/{hash_string}.json', headers=headers)
        output = json.loads(url.text)
        hash_info = json.dumps(output, indent=2)
        return hash_info
    except Exception as e:
        logging.warning(e)

@router.message(F.text.startswith(cfg.all_commands['check_hash']))
async def check_hash(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 2:
            await message.answer(f'<b>{check_hash_string(msg[1])}</b>', disable_web_page_preview=True)
        else:
            await message.answer(f'Пример:\n<code>!check_hash 5f4dcc3b5aa765d61d8327deb882cf99</code>')
    except Exception as e:
        logging.warning(e)
