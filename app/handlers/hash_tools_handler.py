from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
from app.helpers.hash_tools import hash_analyze

router: Router = Router()


@router.message(F.text.startswith(cfg.all_commands['hash_alz_cmds']))
async def send_text2hex_string(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer(f'Пример:\n<code>!hash a6105c0a611b41b08f1209506350279e</code>')
        else:
            hash_string = message.text[6:]
            text = f''''''
            for item in hash_analyze(hash_string):
                text += "<b>Hash type: </b>" + "<code>" + item['name'] + "</code>" + '\n'
                text += "<b>John format: </b>" + "<code>" + str(item['john']) + "</code>" + '\n'
                text += "<b>Hashcat format: </b>" + "<code>" + str(item['hashcat']) + "</code>" + '\n'
                text += "<b>Info: </b>" + "<code>" + str(item['description']) + "</code>" + '\n'
                text += "-" * 10 + "\n"
            await message.answer("Основные варианты:\n" + text)
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
