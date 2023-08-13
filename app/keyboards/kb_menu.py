from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import html
import random as rand
from app.config import cfg
from app.texts import revshells
from app.texts.sqli_examples import sqli_example
from icecream import ic

router: Router = Router()


@router.message(F.text.in_(cfg.all_commands['menu_cmds']))
async def menu_buttons(message: Message):
    try:
        builder = InlineKeyboardBuilder()
        builder.add(InlineKeyboardButton(text="🎩 Pentest HaT", callback_data="pt_hat_channel"))
        builder.add(InlineKeyboardButton(text="⚙️ Commands", callback_data="bot_commands"))
        builder.add(InlineKeyboardButton(text="🔧 Base tools", callback_data="base_tools"))
        builder.add(InlineKeyboardButton(text="🔌 Revshell", callback_data="rev_shell"))
        builder.add(InlineKeyboardButton(text="🔍 Port checker", callback_data="port_checker"))
        builder.add(InlineKeyboardButton(text="🔎 Whois domain", callback_data="whois_domain"))
        builder.add(InlineKeyboardButton(text="📄 DNS records", callback_data="dns_records"))
        builder.add(InlineKeyboardButton(text="🛰 Поиск эксплоита", callback_data="search_sploit"))
        builder.add(InlineKeyboardButton(text="🔮 Hash identify", callback_data="hash_identify"))
        builder.add(InlineKeyboardButton(text="🔓 JWT Decode", callback_data="jwt_decode"))
        builder.add(InlineKeyboardButton(text="💉 SQLi", callback_data="sqli_payloads"))
        builder.add(InlineKeyboardButton(text="🤖 File IDs bot", callback_data="file_id_bot"))
        builder.adjust(2)
        await message.answer(
            "🛡 Меню",
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


@router.callback_query(F.data == 'port_checker')
async def port_check_info(callback: CallbackQuery):
    await callback.message.answer('<code>!port yandex.ru 443</code>')
    await callback.answer()


@router.callback_query(F.data == 'whois_domain')
async def whois_domain_info(callback: CallbackQuery):
    await callback.message.answer('<code>!whois yandex.ru</code>')
    await callback.answer()


@router.callback_query(F.data == 'dns_records')
async def dig_info(callback: CallbackQuery):
    await callback.message.answer(
        '<code>!dig ya.ru</code>\nor\n<code>!dig ya.ru MX)</code>\n\nhttps://en.wikipedia.org/wiki/List_of_DNS_record_types')
    await callback.answer()


@router.callback_query(F.data == 'search_sploit')
async def send_searchsploit_cmd(callback: CallbackQuery):
    await callback.message.answer(f'<code>!ss Microsoft Exchange 2019</code>')
    await callback.answer()


@router.callback_query(F.data == 'sqli_payloads')
async def send_group_link(callback: CallbackQuery):
    await callback.message.answer(f'{sqli_example}')
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
        await callback.message.answer(
            f'Пример:\n<code>!jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTY5MTAxMjU3MSwiZXhwIjoxNjkxMDE2MTcxfQ.BNM4pLUB6wYlnXC0NvHiShDIM6KtIk81prLW8VBCZ88</code>')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'base_tools')
async def send_base_tools_description(callback: CallbackQuery):
    try:
        await callback.message.answer(f'''
Пример:
<code>!b64d UGVudGVzdCBIYVQ=</code>

Пример:
<code>!b64e Pentest Hacks and Tools</code>''')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'hash_identify')
async def send_hash_ident_help(callback: CallbackQuery):
    try:
        await callback.message.answer(f'''
Пример:
<code>!hash a6105c0a611b41b08f1209506350279e</code>''')
        await callback.answer()
    except Exception as e:
        ic(e)
