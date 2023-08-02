from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic

router: Router = Router()
menu_commands = ['!id']


@router.message(F.text.in_(menu_commands))
async def show_menu(message: Message):
    try:
        if message.from_user.id != 539491282:
            logging.info(message.from_user)
        await message.answer(f'<b>ID:</b> <code>{message.from_user.id}</code>')
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')


@router.message(F.new_chat_members)
async def new_members_handler(message: Message):
    try:
        new_member = message.new_chat_members[0]
        await cfg.bot.send_message(message.chat.id, f"Добро пожаловать в HaT 🖖, @{new_member.username} ! 🎩🎩🎩")
    except Exception as e:
        logging.error(f'{e}')
        ic(e)
