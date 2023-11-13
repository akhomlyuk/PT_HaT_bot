from aiogram import Router, F
from aiogram.types import Message, FSInputFile
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import logging
import app.config.cfg as cfg
from icecream import ic
from sys import platform
import os
import time
import random

router: Router = Router()

t = round(time.time())

if platform == "win32":
    path = os.path.expanduser('~')
else:
    os.makedirs('/home/rht_info_bot/PT_HaT_bot/app/static/qrs', exist_ok=True)
    path = os.path.expanduser('~') + r'/PT_HaT_bot/app/static/qrs/'


@router.message(F.text.startswith(cfg.all_commands['qr_cmds']))
async def send_qr(message: Message):
    try:
        msg = message.text.split()
        qr_text = message.text
        if len(msg) == 1:
            await message.answer(f'!qr some text data')
        else:

            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_Q, border=1, box_size=12, version=4)
            qr.add_data(qr_text[3:])
            random.seed(t)
            rng = random.randint(0, 255)
            img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer(),
                                color_mask=RadialGradiantColorMask(edge_color=(rng, 255, rng)))
            img.save(path + 'qr-' + str(t) + '.png', format='PNG')

            photo = FSInputFile(path + 'qr-' + str(t) + '.png', filename='qr-' + str(t) + '.png')
            await message.answer_photo(photo)
            img.close()
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
