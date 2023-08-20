from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
from app.helpers.ctftime_parser import rht_info

router: Router = Router()

rht_info = rht_info()
rht_summary = f'''🌍 Worldwide position: <b>{rht_info["rating"]["2023"]["rating_place"]}</b>
🇷🇺 RU position: <b>{rht_info["rating"]["2023"]["country_place"]}</b>
🎯 Rating points: <b>{rht_info["rating"]["2023"]["rating_points"]}</b>
🚩 Team ID: <b>{rht_info["id"]}</b>
https://ctftime.org/team/186788'''


@router.message(F.text.startswith(cfg.all_commands['team_cmds']))
async def send_ssti_identify(message: Message):
    try:
        await message.answer(f'{rht_summary}')
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
