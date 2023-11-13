from aiogram import Router, F
from aiogram.types import Message, FSInputFile
import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers.pil import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask
import logging
import app.config.cfg as cfg
from app.config.cfg import bot
from icecream import ic
from sys import platform
import os
import time

router: Router = Router()

t = time.time()

if platform == "win32":
    path = os.path.expanduser('~') + r'\qr-' + str(t) + '.png'
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

            qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_L)
            qr.add_data(qr_text[3:])

            img_1 = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
            img_2 = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
            img_3 = qr.make_image(image_factory=StyledPilImage, embeded_image_path=path + 'qr-' + str(t) + '.png')
            ic(img_3)
            photo = FSInputFile(path + 'qr-' + str(t) + '.png', 'qr-' + str(t) + '.png')
            ic(photo)
            ic(path + 'qr-' + str(t) + '.png', 'qr-' + str(t) + '.png')
            await message.answer_photo(photo)
    except Exception as e:
        logging.warning(e)
        ic(e)
        ic()
