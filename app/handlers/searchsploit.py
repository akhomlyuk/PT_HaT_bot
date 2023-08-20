from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import subprocess
import json

router: Router = Router()


@router.message(F.text.startswith(cfg.all_commands['search_sploit_cmds']))
async def search_sploit(message: Message):
    try:
        msg = message.text.split()
        msg2 = message.text[4:].split()
        if len(msg) == 1:
            await message.answer('<code>!ss Microsoft Exchange 2019</code>')
        else:
            sploit_string = ' '.join(msg2)
            command = f"searchsploit {sploit_string} -j -w"
            output_file = "sploit.json"
            subprocess.run(f"{command} > {output_file}", shell=True)
            with open(output_file, "r") as file:
                data = json.load(file)
            lst = []
            for item in data["RESULTS_EXPLOIT"][:10]:
                lst.append('<b>' + item['Title'].replace("<", "to") + '</b>' + '\n' + item['URL'] + '\n' + '-' * 20 + '\n')
            if len(data["RESULTS_EXPLOIT"]) > 10:
                await message.answer(f'<b>Выведены первые 10</b>:\n\n{"".join(lst)}', disable_web_page_preview=True)
            else:
                await message.answer(f'{"".join(lst)}', disable_web_page_preview=True)
    except Exception as e:
        await message.answer(f'Ничего не найдено 😞\nПопробуй изменить запрос')
        ic()
        ic(e)
        logging.error(e)
