import requests
import random
import json
from icecream import ic
from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg

router: Router = Router()


def get_free_gpt_list():
    try:
        r = requests.get('https://raw.githubusercontent.com/LiLittleCat/awesome-free-chatgpt/main/urls.json')
        gpt_list = json.loads(r.text)
        randomized_urls = random.sample(gpt_list, 10)
        return randomized_urls
    except Exception as e:
        ic(e)
        ic()
        logging.error(e)


@router.message(F.text.in_(cfg.all_commands['gpt_cmds']))
async def send_freegpt_list(message: Message):
    try:
        await message.answer(f"{get_free_gpt_list()}")
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
