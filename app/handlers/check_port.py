from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import socket

router: Router = Router()


def check_port(host: str, port: int):
    try:
        blocklist = ['127.0.0.1', 'localhost', '0.0.0.0']
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)
        if host not in blocklist:
            s.connect((host, port))
            s.close()
            return f"Port {port} on {host} is open 😄"
        else:
            return f"Good luck bro! 😄😄😄"
    except socket.error:
        return f"Port {port} closed or filtered 😞"


@router.message(F.text.startswith(cfg.all_commands['checkport_cmds']))
async def search_sploit(message: Message):
    try:
        msg = message.text.split()
        if len(msg) == 1:
            await message.answer('<code>!port yandex.ru 443</code>')
        elif len(msg) != 3:
            await message.answer(f'<code>!port yandex.ru 443</code>')
        else:
            await message.answer(f"{check_port(msg[1], int(msg[2]))}")
    except Exception as e:
        ic()
        ic(e)
        logging.error(e)
