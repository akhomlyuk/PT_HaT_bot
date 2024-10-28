from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery, URLInputFile
from aiogram.utils.keyboard import InlineKeyboardBuilder
from aiogram import html
from app.config import cfg
from app.config.cfg import bot
from app.texts import revshells, description
from app.texts.sqli_examples import sqli_example
from app.helpers.ctftime_parser import rht_info
from app.handlers.ctftime_handler import rht_summary, top10_results
from icecream import ic
import random as rand

router: Router = Router()

rht_info = rht_info()


@router.message(F.text.in_(cfg.all_commands['menu_cmds']))
async def menu_buttons(message: Message):
    try:
        builder = InlineKeyboardBuilder()
        builder.add(InlineKeyboardButton(text="🎩 Pentest HaT", callback_data="pt_hat_channel"))
        builder.add(InlineKeyboardButton(text="⚙️ Commands", callback_data="bot_commands"))
        builder.add(InlineKeyboardButton(text="🚩 RHTeam", callback_data="rht_info"))
        builder.add(InlineKeyboardButton(text="🏆 Лучшие результаты", callback_data="best_results"))
        builder.add(InlineKeyboardButton(text="📑 Free socks/http proxy", callback_data="free_proxy"))
        builder.add(InlineKeyboardButton(text="🇷🇺 Команды России", callback_data="top_ru"))
        builder.add(InlineKeyboardButton(text="🔧 Base tools", callback_data="base_tools"))
        builder.add(InlineKeyboardButton(text="🔌 Revshell", callback_data="rev_shell"))
        builder.add(InlineKeyboardButton(text="🔍 Port checker", callback_data="port_checker"))
        builder.add(InlineKeyboardButton(text="🔎 Whois domain", callback_data="whois_domain"))
        builder.add(InlineKeyboardButton(text="📄 DNS records", callback_data="dns_records"))
        builder.add(InlineKeyboardButton(text="🛰 Поиск эксплоита", callback_data="search_sploit"))
        builder.add(InlineKeyboardButton(text="🔮 Hash identify", callback_data="hash_identify"))
        builder.add(InlineKeyboardButton(text="🔓 JWT Decode", callback_data="jwt_decode"))
        builder.add(InlineKeyboardButton(text="💉 SQLi", callback_data="sqli_payloads"))
        builder.add(InlineKeyboardButton(text="🐍 Python easy!", callback_data="python_easy"))
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
@router.callback_query(F.data == 'rht_info')
async def send_rht_info(callback: CallbackQuery):
    await callback.message.answer(f'{rht_summary}\n\nFrom: @{callback.from_user.username}')
    await callback.answer()


@router.callback_query(F.data == 'free_proxy')
async def send_proxy_info(callback: CallbackQuery):
    await callback.message.answer(f'{description.show_proxies_help}'
                                  f'\n\nFrom: @{callback.from_user.username}')
    await callback.answer()


@router.callback_query(F.data == 'best_results')
async def send_best_results(callback: CallbackQuery):
    await callback.message.answer(f'<b>Лучшие результаты по рейтингу</b>\n\n{top10_results}\n\n'
                                  f'🎯 Rating points: <b>{rht_info["rating"]["2024"]["rating_points"]}</b>'
                                  f'\nFrom: @{callback.from_user.username}', disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(F.data == 'top_ru')
async def send_top_ru(callback: CallbackQuery):
    top_ru = top_teams_ru()
    top = '\n'.join(str(team) for team in top_ru)
    await callback.message.answer(f'🇷🇺 <b>Топ команд России</b>: 🇷🇺\n\n{top}\n\nhttps://ctftime.org/stats/RU'
                                  f'\n\nFrom: @{callback.from_user.username}', disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(F.data == 'pt_hat_channel')
async def send_channel_link(callback: CallbackQuery):
    await callback.message.answer(f'https://t.me/pt_soft '
                                  f'\n\nFrom: @{callback.from_user.username}')
    await callback.answer()


@router.callback_query(F.data == 'python_easy')
async def send_python_onepic(callback: CallbackQuery):
    photo = URLInputFile('https://raw.githubusercontent.com/coreb1t/awesome-pentest-cheat-sheets/master/docs/python-3-in-one-pic.png',
                         bot=bot, filename='python3_onepic.png')
    await callback.message.answer_document(photo)
    await callback.answer()


@router.callback_query(F.data == 'port_checker')
async def port_check_info(callback: CallbackQuery):
    await callback.message.answer(f'Пример:\n<code>!port yandex.ru 443</code>'
                                  f'\n\nFrom: @{callback.from_user.username}')
    await callback.answer()


@router.callback_query(F.data == 'whois_domain')
async def whois_domain_info(callback: CallbackQuery):
    await callback.message.answer(f'Пример:\n<code>!whois yandex.ru</code>'
                                  f'\n\nFrom: @{callback.from_user.username}')
    await callback.answer()


@router.callback_query(F.data == 'dns_records')
async def dig_info(callback: CallbackQuery):
    await callback.message.answer(
        f'Пример:\n<code>!dig ya.ru</code>\nor\n<code>!dig ya.ru MX</code>\n\nhttps://en.wikipedia.org/wiki/List_of_DNS_record_types '
        f'\n\nFrom: @{callback.from_user.username}',
        disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(F.data == 'search_sploit')
async def send_searchsploit_cmd(callback: CallbackQuery):
    await callback.message.answer(f'Пример:\n<code>!ss Microsoft Exchange 2019</code>'
                                  f'\n\nFrom: @{callback.from_user.username}')
    await callback.answer()


@router.callback_query(F.data == 'sqli_payloads')
async def send_group_link(callback: CallbackQuery):
    await callback.message.answer(f'{sqli_example}'
                                  f'\n\nFrom: @{callback.from_user.username}', disable_web_page_preview=True)
    await callback.answer()


@router.callback_query(F.data == 'rev_shell')
async def send_revshell(callback: CallbackQuery):
    try:
        await callback.message.answer(f'<code>{html.quote(rand.choice(revshells.shells))}</code>'
                                      f'\n\nFrom: @{callback.from_user.username}')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'bot_commands')
async def send_bot_commands(callback: CallbackQuery):
    try:
        await callback.message.answer(f'{cfg.bot_commands}'
                                      f'\n\nFrom: @{callback.from_user.username}')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'file_id_bot')
async def send_fileid_bot_link(callback: CallbackQuery):
    try:
        await callback.message.answer(f'Отправить любой файл или сообщение: @File_IDs_bot '
                                      f'\n\nFrom: @{callback.from_user.username}')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'jwt_decode')
async def send_fileid_bot_link(callback: CallbackQuery):
    try:
        await callback.message.answer(
            f'Пример:\n<code>!jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTY5MTAxMjU3MSwiZXhwIjoxNjkxMDE2MTcxfQ.BNM4pLUB6wYlnXC0NvHiShDIM6KtIk81prLW8VBCZ88</code>'
            f'\n\nFrom: @{callback.from_user.username}')
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
<code>!b64e Pentest Hacks and Tools</code>
\n\nFrom: @{callback.from_user.username}''')
        await callback.answer()
    except Exception as e:
        ic(e)


@router.callback_query(F.data == 'hash_identify')
async def send_hash_ident_help(callback: CallbackQuery):
    try:
        await callback.message.answer(f'''
Пример:
<code>!hash a6105c0a611b41b08f1209506350279e</code>\n\nFrom: @{callback.from_user.username}''')
        await callback.answer()
    except Exception as e:
        ic(e)
