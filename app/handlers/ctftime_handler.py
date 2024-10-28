from aiogram import Router, F
from aiogram.types import Message
from app.config import cfg
from icecream import ic
from app.helpers.ctftime_parser import rht_info, rht_best_res
import logging

router: Router = Router()

rht_info = rht_info()
rht_best = rht_best_res()


rht_summary = f'''🌍 Worldwide position: <b>{rht_info["rating"]["2024"]["rating_place"]}</b>
🇷🇺 RU position: <b>{rht_info["rating"]["2024"]["country_place"]}</b>
🎯 Rating points: <b>{rht_info["rating"]["2024"]["rating_points"]}</b>
🚩 Team ID: <b>{rht_info["id"]}</b>
https://ctftime.org/team/186788'''

top10_results = '\n'.join([i for i in rht_best[1]])


@router.message(F.text.startswith(cfg.all_commands['team_cmds']))
async def rhteam_info(message: Message):
    try:
        await message.answer(f'{rht_summary}')
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
        pass


# @router.message(F.text.startswith(cfg.all_commands['topteams_cmds']))
# async def top_teams_ru(message: Message):
#     try:
#         top = '\n'.join(str(team) for team in top_ru)
#         await message.answer(f'🇷🇺 <b>Топ команд России</b>: 🇷🇺\n\n{top}\n\nhttps://ctftime.org/stats/RU', disable_web_page_preview=True)
#     except Exception as e:
#         ic()
#         ic(e)
#         logging.error(e)
#         pass


@router.message(F.text.startswith(cfg.all_commands['bestres_cmds']))
async def rhteam_best(message: Message):
    try:
        await message.answer(f'<b>Лучшие результаты по рейтингу</b>\n\n{top10_results}\n\n'
                             # f'<b>Organized CTF events</b>\n▪️ Cybercoliseum: <b>{22.83 * 2}</b>\n▪️ Cybercoliseum II: <b>{20.60 * 2}</b>\n\n'
                             f'🎯 Rating points: <b>{rht_info["rating"]["2024"]["rating_points"]}</b>',
                             disable_web_page_preview=True)
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
        pass
