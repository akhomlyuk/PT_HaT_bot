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
        json_data = json.dumps(randomized_urls, indent=2)
        return randomized_urls
    except Exception as e:
        ic(e)
        ic()
        logging.error(e)


@router.message(F.text.in_(cfg.all_commands['gpt_cmds']))
async def send_freegpt_list(message: Message):
    try:
        gpt_list = "\n".join(str(i) for i in get_free_gpt_list())
        await message.answer(f'Список случайных GPT ботов:\n{gpt_list}', disable_web_page_preview=True)
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
