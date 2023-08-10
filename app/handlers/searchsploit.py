from aiogram import Router, F, html
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import os
import subprocess
import json

router: Router = Router()


@router.message(F.text.startswith('!ss'))
async def search_sploit(message: Message):
    try:
        msg = message.text.split()
        msg2 = message.text[4:].split()
        if len(msg) == 1:
            await message.answer('<code>!ss Microsoft Exchange 2019</code>')
        else:
            sploit_string = ' '.join(msg2)
            ic(sploit_string)
            logging.critical(sploit_string)
            command = f"searchsploit {sploit_string} -j -w"
            logging.critical(command)
            output_file = "sploit.json"
            logging.critical(output_file)
            subprocess.run(f"{command} > {output_file}", shell=True)
            with open(output_file, "r") as file:
                data = json.load(file)
            data_out = json.dumps(data, indent=2)
            await message.answer(f'{data["RESULTS_EXPLOIT"]}', disable_web_page_preview=True)
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
