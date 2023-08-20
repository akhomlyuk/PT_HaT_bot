from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
from app.helpers.ctftime_parser import rht_info, rht_best_res, top_teams_ru

router: Router = Router()

rht_info = rht_info()
rht_best = rht_best_res()
top_ru = top_teams_ru()

rht_summary = f'''🌍 Worldwide position: <b>{rht_info["rating"]["2023"]["rating_place"]}</b>
🇷🇺 RU position: <b>{rht_info["rating"]["2023"]["country_place"]}</b>
🎯 Rating points: <b>{rht_info["rating"]["2023"]["rating_points"]}</b>
🚩 Team ID: <b>{rht_info["id"]}</b>
https://ctftime.org/team/186788'''


@router.message(F.text.startswith(cfg.all_commands['team_cmds']))
async def rhteam_info(message: Message):
    try:
        await message.answer(f'{rht_summary}')
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)


@router.message(F.text.startswith(cfg.all_commands['topteams_cmds']))
async def top_teams_ru(message: Message):
    try:
        top = '\n'.join(str(team) for team in top_ru)
        await message.answer(f'🇷🇺 <b>Топ команд по России</b>: 🇷🇺\n\n{top}\nhttps://ctftime.org/stats/RU')
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
