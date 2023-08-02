from aiogram import Router, F, html
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from app.helpers.revshell import generate_revshell
from icecream import ic

router: Router = Router()
id_commands = ['!id']


@router.message(F.text.in_(id_commands))
async def show_menu(message: Message):
    try:
        if message.from_user.id != 539491282:
            logging.info(message.from_user)
        await message.answer(f'<b>ID:</b> <code>{message.from_user.id}</code>')
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')


@router.message(F.text.startswith('!rev'))
async def send_rev_shell(message: Message):
    try:
        msg = message.text
        msg = msg.split(' ')
        if len(msg) != 3:
            await message.answer(f'Пример: <code>!rev 127.0.0.1 31337</code>')
        else:
            await message.answer(f'<code>{html.quote(generate_revshell(msg[1], int(msg[2])))}</code>')
    except Exception as e:
        logging.warning(e)
        ic(e)


@router.message(F.new_chat_members)
async def new_members_handler(message: Message):
    try:
        new_member = message.new_chat_members[0]
        await cfg.bot.send_message(message.chat.id, f"Добро пожаловать в HaT 🖖, @{new_member.username} ! 🎩🎩🎩")
    except Exception as e:
        logging.error(f'{e}')
        ic(e)
