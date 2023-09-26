from aiogram import Router, F
from aiogram.types import Message
import app.config.cfg as cfg
from icecream import ic
import random
import os
from sys import platform
from ..texts import description

router: Router = Router()

proxies_path = os.path.expanduser('~')

if platform == "win32":
    with open(proxies_path + r'\proxies\proxies\socks5.txt', 'r') as socks5_file:
        socks5_file = socks5_file.read()
    with open(proxies_path + r'\proxies\proxies\http.txt', 'r') as http_file:
        http_file = http_file.read()
    with open(proxies_path + r'\proxies\proxies\socks4.txt', 'r') as socks4_file:
        socks4_file = socks4_file.read()
else:
    with open(proxies_path + r'/proxies/proxies/socks5.txt', 'r') as socks5_file:
        socks5_file = socks5_file.read()
    with open(proxies_path + r'/proxies/proxies/http.txt', 'r') as http_file:
        http_file = http_file.read()
    with open(proxies_path + r'/proxies/proxies/socks4.txt', 'r') as socks4_file:
        socks4_file = socks4_file.read()

if platform == "win32":
    with open(proxies_path + r'\proxies\proxies_geolocation\socks5.txt', 'r') as socks5_file_geo:
        socks5_file_geo = socks5_file_geo.read()
    with open(proxies_path + r'\proxies\proxies_geolocation\http.txt', 'r') as http_file_geo:
        http_file_geo = http_file_geo.read()
    with open(proxies_path + r'\proxies\proxies_geolocation\socks4.txt', 'r') as socks4_file_geo:
        socks4_file_geo = socks4_file_geo.read()
else:
    with open(proxies_path + r'/proxies/proxies_geolocation/socks5.txt', 'r') as socks5_file_geo:
        socks5_file_geo = socks5_file_geo.read()
    with open(proxies_path + r'/proxies/proxies_geolocation/http.txt', 'r') as http_file_geo:
        http_file_geo = http_file_geo.read()
    with open(proxies_path + r'/proxies/proxies_geolocation/socks4.txt', 'r') as socks4_file_geo:
        socks4_file_geo = socks4_file_geo.read()

socks5_lst = list(socks5_file.split('\n'))
random_socks5 = random.choices(socks5_lst, k=3)

socks4_lst = list(socks4_file.split('\n'))
random_socks4 = random.choices(socks5_lst, k=3)

http_lst = list(http_file.split('\n'))
random_http = random.choices(http_lst, k=3)

socks5_lst_geo = list(socks5_file_geo.split('\n'))
random_socks5_geo = random.choices(socks5_lst_geo, k=3)

socks4_lst_geo = list(socks4_file_geo.split('\n'))
random_socks4_geo = random.choices(socks4_lst_geo, k=3)

http_lst_geo = list(http_file_geo.split('\n'))
random_http_geo = random.choices(http_lst_geo, k=3)


@router.message(F.text.startswith(cfg.all_commands['socks5_cmds']))
async def get_socks5_proxy(message: Message):
    try:
        args = message.text.split()
        newline = '\n'
        if len(args) == 1:
            await message.answer(f"<b>Socks5 proxies:</b>\n<code>{newline.join(random_socks5)}</code>")
        elif len(args) == 2:
            try:
                if 1 <= int(args[1]) <= 20:
                    await message.answer(f"<b>Socks5 proxies:</b>\n<code>{newline.join(random.choices(socks5_lst, k=int(args[1])))}</code>")
                else:
                    await message.answer(f"<b>Usage:</b>\n<code>!socks5 1...20</code>\n<code>!socks5 1...20 geo</code>")
            except ValueError:
                await message.answer(f"<b>Usage:</b>\n<code>!socks5 1...20</code>\n<code>!socks5 1...20 geo</code>")
        elif len(args) == 3:
            if args[2] == "geo" and 1 <= int(args[1]) <= 20:
                await message.answer(f"<b>Socks5 proxies with geo:</b>\n"
                                     f"<code>{newline.join(random.choices(socks5_lst_geo, k=int(args[1])))}</code>")
            else:
                await message.answer(f"<b>Usage:</b>\n<code>!socks5 1...20 geo</code>")
    except Exception as e:
        ic()
        ic(e)


@router.message(F.text.startswith(cfg.all_commands['socks4_cmds']))
async def get_socks4_proxy(message: Message):
    try:
        args = message.text.split()
        newline = '\n'
        if len(args) == 1:
            await message.answer(f"<b>Socks4 proxies:</b>\n<code>{newline.join(random_socks4)}</code>")
        elif len(args) == 2:
            try:
                if 1 <= int(args[1]) <= 20:
                    await message.answer(f"<b>Socks4 proxies:</b>\n<code>{newline.join(random.choices(socks4_lst, k=int(args[1])))}</code>")
                else:
                    await message.answer(f"<b>Usage:</b>\n<code>!socks4 1...20</code>")
            except ValueError:
                await message.answer(f"<b>Usage:</b>\n<code>!socks4 1...20</code>\n<code>!socks4 1...20 geo</code>")
        elif len(args) == 3:
            if args[2] == "geo" and 1 <= int(args[1]) <= 20:
                await message.answer(f"<b>Socks4 proxies with geo:</b>\n"
                                     f"<code>{newline.join(random.choices(socks4_lst_geo, k=int(args[1])))}</code>")
            else:
                await message.answer(f"<b>Usage:</b>\n<code>!socks4 1...20 geo</code>")

    except Exception as e:
        ic()
        ic(e)


@router.message(F.text.startswith(cfg.all_commands['proxy_cmds']))
async def get_http_proxy(message: Message):
    try:
        args = message.text.split()
        newline = '\n'
        if len(args) == 1:
            await message.answer(f"<b>Http proxies:</b>\n<code>{newline.join(random_http)}</code>")
        elif len(args) == 2:
            try:
                if 1 <= int(args[1]) <= 20:
                    await message.answer(f"<b>Http proxies:</b>\n<code>{newline.join(random.choices(http_lst, k=int(args[1])))}</code>")
                else:
                    await message.answer(f"<b>Usage:</b>\n<code>!http 1...20</code>")
            except ValueError:
                await message.answer(f"<b>Usage:</b>\n<code>!http 1...20</code>\n<code>!http 1...20 geo</code>")
        elif len(args) == 3:
            if args[2] == "geo" and 1 <= int(args[1]) <= 20:
                await message.answer(f"<b>Http proxies with geo:</b>\n"
                                     f"<code>{newline.join(random.choices(http_lst_geo, k=int(args[1])))}</code>")
            else:
                await message.answer(f"<b>Usage:</b>\n<code>!http 1...20 geo</code>")

    except Exception as e:
        ic()
        ic(e)


@router.message(F.text.startswith(cfg.all_commands['proxies_cmds']))
async def get_proxies_help(message: Message):
    try:
        await message.answer(f"<b>Socks5</b>: {len(socks5_lst)}\n"
                             f"<b>Socks4</b>: {len(socks4_lst)}\n"
                             f"<b>Http</b>: {len(http_lst)}\n\n"
                             f"{description.show_proxies_help}")
    except Exception as e:
        ic()
        ic(e)
