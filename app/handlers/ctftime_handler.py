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

top10_results = f'''<b>Лучшие результаты по рейтингу</b>\n
{rht_best[2][0]}
{rht_best[2][1]}
{rht_best[2][2]}
{rht_best[2][3]}
{rht_best[2][4]}
{rht_best[2][5]}
{rht_best[2][6]}
{rht_best[2][7]}
{rht_best[2][8]}'''


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
        await message.answer(f'🇷🇺 <b>Топ команд по России</b>: 🇷🇺\n\n{top}\n\nhttps://ctftime.org/stats/RU', disable_web_page_preview=True)
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)


@router.message(F.text.startswith(cfg.all_commands['bestres_cmds']))
async def rhteam_best(message: Message):
    try:
        await message.answer(f'{top10_results}', disable_web_page_preview=True)
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
