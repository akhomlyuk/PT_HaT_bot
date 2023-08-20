from aiogram import Router, F
from aiogram.types import Message, URLInputFile
import logging
import app.config.cfg as cfg
from app.config.cfg import bot
from icecream import ic

router: Router = Router()


@router.message(F.text.startswith(cfg.all_commands['ssti_cmds']))
async def send_ssti_identify(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            photo = URLInputFile('https://1517081779-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-L_2uGJGU7AVNRcqRvEi%2F-M7O4Hp6bOFFkge_yq4G%2F-M7OCvxwZCiaP8Whx2fi%2Fimage.png?alt=media&token=4b40cf58-5561-4925-bc86-1d4689ca53d1', bot=bot)
            await message.answer_photo(photo,
                                       caption='\nhttps://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection')
        else:
            await message.answer(f'https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection')
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
