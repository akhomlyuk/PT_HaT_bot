from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic

router: Router = Router()


@router.message(F.text.startswith(cfg.all_commands['ban_cmds']))
async def ban_user(message: Message):
    try:
        if message.from_user.id in cfg.admins:
            await message.bot.ban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f'Пользователь <b>{message.reply_to_message.from_user.first_name}</b> заблокирован!')
        else:
            await message.answer(f'Недостаточно прав')
    except Exception as e:
        logging.error(e)
        ic(e)
        await message.answer(f'{e}')


@router.message(F.text.startswith(cfg.all_commands['unban_cmds']))
async def unban_user(message: Message):
    try:
        if message.from_user.id in cfg.admins:
            await message.bot.unban_chat_member(message.chat.id, message.reply_to_message.from_user.id)
            await message.answer(f'Пользователь <b>{message.reply_to_message.from_user.first_name}</b> разблокирован!')
        else:
            await message.answer(f'Недостаточно прав')
    except Exception as e:
        logging.error(e)
        ic(e)
        await message.answer(f'{e}')
