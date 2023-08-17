from aiogram import Router, F
from aiogram.types import Message, URLInputFile, FSInputFile
import logging
import app.config.cfg as cfg
from icecream import ic

router: Router = Router()


@router.message(F.text.startswith(cfg.all_commands['ssti_cmds']))
async def send_ssti_identify(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer_photo('AgACAgIAAxkBAAIF_mTeHJWrQxmkISotQYadLk-iOW_qAAL70zEbb7LwSqnZnI0KVt_UAQADAgADeAADMAQ',
                                       caption='\nhttps://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection')
        else:
            msg2 = message.text[5:]
            await message.answer(f'not ready yet')
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
