from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import html
import random as rand
from app.config import cfg
from app.texts import revshells
from icecream import ic

router: Router = Router()


@router.message(F.text.in_(cfg.all_commands['menu_cmds']))
async def menu_buttons(message: Message):
    try:
        builder = InlineKeyboardBuilder()
        builder.add(InlineKeyboardButton(text="🎩 Pentest HaT", callback_data="pt_hat_channel"))
        builder.add(InlineKeyboardButton(text="🔧 Base tools", callback_data="base_tools"))
        builder.add(InlineKeyboardButton(text="🔌 Revshell", callback_data="rev_shell"))
        builder.add(InlineKeyboardButton(text="🔓 JWT Decode", callback_data="jwt_decode"))
        builder.add(InlineKeyboardButton(text="⚙️ Commands", callback_data="bot_commands"))
        builder.add(InlineKeyboardButton(text="🤖 File IDs bot", callback_data="file_id_bot"))
        builder.adjust(2)
        await message.answer(
            "Меню:",
            reply_markup=builder.as_markup()
        )
    except Exception as e:
        ic(e)
        await message.answer(str(e))


# Коллбеки для пунктов меню
@router.callback_query(F.data == 'pt_hat_channel')
async def send_channel_link(callback: CallbackQuery):
    await callback.message.answer('https://t.me/pt_soft')
    await callback.answer()


@router.callback_query(F.data == 'pt_hat_group')
async def send_group_link(callback: CallbackQuery):
    await callback.message.answer('https://t.me/pt_hat')
    await callback.answer()


@router.callback_query(F.data == 'rev_shell')
async def send_revshell(callback: CallbackQuery):
    try:
        await callback.message.answer(f'<code>{html.quote(rand.choice(revshells.shells))}</code>')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'bot_commands')
async def send_bot_commands(callback: CallbackQuery):
    try:
        await callback.message.answer(f'{cfg.bot_commands}')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'file_id_bot')
async def send_fileid_bot_link(callback: CallbackQuery):
    try:
        await callback.message.answer(f'Отправить любой файл или сообщение: @File_IDs_bot')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'jwt_decode')
async def send_fileid_bot_link(callback: CallbackQuery):
    try:
        await callback.message.answer(f'Пример:\n<code>!jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTY5MTAxMjU3MSwiZXhwIjoxNjkxMDE2MTcxfQ.BNM4pLUB6wYlnXC0NvHiShDIM6KtIk81prLW8VBCZ88</code>')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'base_tools')
async def send_base_tools_description(callback: CallbackQuery):
    try:
        await callback.message.answer(f'''
Пример:
<code>!b64_decode UGVudGVzdCBIYVQ=</code>

Пример:
<code>!b64_encode Pentest HaT</code>''')
        await callback.answer()
    except Exception as e:
        ic(e)
