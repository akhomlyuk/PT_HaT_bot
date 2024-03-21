from aiogram import Router, F, types
from aiogram.types import Message
from aiogram.filters.command import Command
from app.texts.description import show_description
import app.config.cfg as cfg
import logging
from icecream import ic

router: Router = Router()


@router.message(Command("start"))
async def cmd_start(message: Message):
    try:
        # if message.from_user.id not in cfg.admins:
        logging.info(f'Бот активирован: {message.from_user}')
        await message.answer(show_description, disable_web_page_preview=True)
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer(show_description, disable_web_page_preview=True)


@router.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="🎯")


@router.message(F.text.in_(cfg.all_commands['help_cmds']))
async def show_info(message: Message):
    try:
        if message.from_user.id not in cfg.admins:
            logging.info(message.from_user)
        await message.answer(show_description, disable_web_page_preview=True)
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')
