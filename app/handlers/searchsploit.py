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
        if len(msg) == 1:
            await message.answer('!ss Microsoft Exchange 2019')
        else:
            sploit_string = ' '.join(msg[1])
            command = f"searchsploit {sploit_string} -j -w"
            output_file = "sploit.json"
            subprocess.run(f"{command} > {output_file}", shell=True)
            with open(output_file, "r") as file:
                data = json.load(file)
            ic(data)
            await message.answer(f'{data}')
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
