from aiogram import Router, F
from aiogram.types import Message, InputFile
import logging
import app.config.cfg as cfg
from icecream import ic

router: Router = Router()


@router.message(F.text.startswith(cfg.all_commands['ssti_cmds']))
async def send_hex2text_string(message: Message):
    try:
        msg = message.text.split()
        photo = InputFile("ssti.webp")

        if len(msg) == 1:
            await message.answer_photo(photo, caption='определяем шаблонизатор')
        # elif len(msg) > 2:
        #     await message.answer(
        #         f'Неправильная hex последовательность\nПример:\n<code>!h2t 50656e74657374204861636b7320616e6420546f6f6c73</code>')
        else:
            msg2 = message.text[5:]
            await message.answer(f'not ready yet')
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()