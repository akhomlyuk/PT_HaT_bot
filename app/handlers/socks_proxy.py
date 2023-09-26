from aiogram import Router, F
from aiogram.types import Message
import app.config.cfg as cfg
from icecream import ic
import random
import os
from sys import platform
from app.texts import description

router: Router = Router()

file_types = ['socks5', 'http', 'socks4']
geo_file_types = ['socks5', 'http', 'socks4']

proxies_path = os.path.expanduser('~')

file_paths = {}
geo_file_paths = {}

if platform == "win32":
    path_separator = '\\'
    proxies_dir = 'proxies' + path_separator + 'proxies'
    geo_dir = 'proxies' + path_separator + 'proxies_geolocation'
else:
    path_separator = '/'
    proxies_dir = 'proxies' + path_separator + 'proxies'
    geo_dir = 'proxies' + path_separator + 'proxies_geolocation'

for file_type in file_types:
    file_path = os.path.join(proxies_path, proxies_dir, file_type + '.txt')
    with open(file_path, 'r') as file:
        file_paths[file_type] = file.read().split('\n')

for file_type in geo_file_types:
    file_path = os.path.join(proxies_path, geo_dir, file_type + '.txt')
    with open(file_path, 'r') as file:
        geo_file_paths[file_type] = file.read().split('\n')

random_socks5 = random.choices(file_paths['socks5'], k=3)
random_socks4 = random.choices(file_paths['socks4'], k=3)
random_http = random.choices(file_paths['http'], k=3)

random_socks5_geo = random.choices(geo_file_paths['socks5'], k=3)
random_socks4_geo = random.choices(geo_file_paths['socks4'], k=3)
random_http_geo = random.choices(geo_file_paths['http'], k=3)


@router.message(F.text.startswith(cfg.all_commands['socks5_cmds']))
async def get_socks5_proxy(message: Message):
    try:
        args = message.text.split()
        nr = '\n'
        if len(args) == 1:
            await message.answer(f"<b>Socks5 proxies:</b>\n<code>{nr.join(random_socks5)}</code>")
        elif len(args) == 2:
            try:
                if 1 <= int(args[1]) <= 20:
                    await message.answer(f"<b>Socks5 proxies:</b>\n<code>{nr.join(random.choices(file_paths['socks5'], k=int(args[1])))}</code>")
                else:
                    await message.answer(f"<b>Usage:</b>\n<code>!socks5 1...20</code>\n<code>!socks5 1...20 geo</code>")
            except ValueError:
                await message.answer(f"<b>Usage:</b>\n<code>!socks5 1...20</code>\n<code>!socks5 1...20 geo</code>")
        elif len(args) == 3:
            if args[2] == "geo" and 1 <= int(args[1]) <= 20:
                await message.answer(f"<b>Socks5 proxies with geo:</b>\n"
                                     f"<code>{nr.join(random.choices(geo_file_paths['socks5'], k=int(args[1])))}</code>")
            else:
                await message.answer(f"<b>Usage:</b>\n<code>!socks5 1...20 geo</code>")
    except Exception as e:
        ic()
        ic(e)


@router.message(F.text.startswith(cfg.all_commands['socks4_cmds']))
async def get_socks4_proxy(message: Message):
    try:
        args = message.text.split()
        nr = '\n'
        if len(args) == 1:
            await message.answer(f"<b>Socks4 proxies:</b>\n<code>{nr.join(random_socks4)}</code>")
        elif len(args) == 2:
            try:
                if 1 <= int(args[1]) <= 20:
                    await message.answer(f"<b>Socks4 proxies:</b>\n<code>{nr.join(random.choices(file_paths['socks4'], k=int(args[1])))}</code>")
                else:
                    await message.answer(f"<b>Usage:</b>\n<code>!socks4 1...20</code>")
            except ValueError:
                await message.answer(f"<b>Usage:</b>\n<code>!socks4 1...20</code>\n<code>!socks4 1...20 geo</code>")
        elif len(args) == 3:
            if args[2] == "geo" and 1 <= int(args[1]) <= 20:
                await message.answer(f"<b>Socks4 proxies with geo:</b>\n"
                                     f"<code>{nr.join(random.choices(geo_file_paths['socks4'], k=int(args[1])))}</code>")
            else:
                await message.answer(f"<b>Usage:</b>\n<code>!socks4 1...20 geo</code>")

    except Exception as e:
        ic()
        ic(e)


@router.message(F.text.startswith(cfg.all_commands['proxy_cmds']))
async def get_http_proxy(message: Message):
    try:
        args = message.text.split()
        nr = '\n'
        if len(args) == 1:
            await message.answer(f"<b>Http proxies:</b>\n<code>{nr.join(random_http)}</code>")
        elif len(args) == 2:
            try:
                if 1 <= int(args[1]) <= 20:
                    await message.answer(f"<b>Http proxies:</b>\n<code>{nr.join(random.choices(file_paths['http'], k=int(args[1])))}</code>")
                else:
                    await message.answer(f"<b>Usage:</b>\n<code>!http 1...20</code>")
            except ValueError:
                await message.answer(f"<b>Usage:</b>\n<code>!http 1...20</code>\n<code>!http 1...20 geo</code>")
        elif len(args) == 3:
            if args[2] == "geo" and 1 <= int(args[1]) <= 20:
                await message.answer(f"<b>Http proxies with geo:</b>\n"
                                     f"<code>{nr.join(random.choices(geo_file_paths['http'], k=int(args[1])))}</code>")
            else:
                await message.answer(f"<b>Usage:</b>\n<code>!http 1...20 geo</code>")

    except Exception as e:
        ic()
        ic(e)


@router.message(F.text.startswith(cfg.all_commands['proxies_cmds']))
async def get_proxies_help(message: Message):
    try:
        await message.answer(f"<b>Socks5</b>: {len(file_paths['socks5'])}\n"
                             f"<b>Socks4</b>: {len(file_paths['socks4'])}\n"
                             f"<b>Http</b>: {len(file_paths['http'])}\n\n"
                             f"{description.show_proxies_help}")
    except Exception as e:
        ic()
        ic(e)
