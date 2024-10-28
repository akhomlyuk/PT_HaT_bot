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
        return json.dumps(output, indent=2)
    except Exception as e:
        logging.warning(e)

@router.message(F.text.in_(cfg.all_commands['check_hash']))
async def check_hash(message: Message):
    try:
        msg = message.text.split()
        await message.answer(f'{check_hash_string(msg[1])}', disable_web_page_preview=True)
    except Exception as e:
        logging.warning(e)
