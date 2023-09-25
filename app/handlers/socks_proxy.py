from aiogram import Router, F
from aiogram.types import Message
import app.config.cfg as cfg
from icecream import ic
import requests
import random

router: Router = Router()

agent = {'User-agent': 'Mozilla/5.0'}
socks5_url = 'https://raw.githubusercontent.com/TheSpeedX/SOCKS-List/master/socks5.txt'
socks5_response = requests.get(socks5_url)

socks5_lst = list(socks5_response.text.split('\n'))
random_proxies = random.choices(socks5_lst, k=50)

url = 'http://ifconfig.me/ip'


@router.message(F.text.in_(cfg.all_commands['proxy_cmds']))
async def get_socks_proxy(message: Message):
    try:
        for proxy in random_proxies:
            try:
                proxy_ip, proxy_port = proxy.split(':')
                proxies = {
                    "http": "socks5://" + proxy,
                    "https": "socks5://" + proxy
                }

                response = requests.get(url, proxies=proxies, timeout=3, headers=agent, verify=False)
                ip = response.text
                if ip == proxy_ip:
                    await message.answer(f"Free proxy: <code>socks5://{proxy}</code>")
                    break
            except Exception as e:
                ic(e)
    except Exception as e:
        ic(e)
