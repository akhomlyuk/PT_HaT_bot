import requests
import random
from icecream import ic
from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg

router: Router = Router()

url = 'https://github.com/scriptzteam/Tor-Bridges-Collector/raw/main/bridges-obfs4'

req = requests.get(url)
bridges = req.text.split('\n')
rnd_bridges = random.choices(bridges, k=10)


@router.message(F.text.in_(cfg.all_commands['bridges']))
async def send_tor_bridges_list(message: Message):
    try:
        nl = "\n"
        await message.answer(f'Мосты(obfs4 bridges) для Tor:\n\n{nl.join(rnd_bridges)}', disable_web_page_preview=True)
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
