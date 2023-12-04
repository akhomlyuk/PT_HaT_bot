from aiogram import Router, F
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import requests
import json

router: Router = Router()


def get_poc(cve: str):
    cve_id = {
        'cve_id': cve,
    }

    response = requests.get('https://poc-in-github.motikan2010.net/api/v1/', params=cve_id)
    dict_response = json.loads(response.text)
    json_r = json.dumps(dict_response, indent=4)
    return json_r


@router.message(F.text.startswith(cfg.all_commands['poc_cmds']))
async def search_poc(message: Message):
    try:
        msg = message.text.split()
        msg2 = message.text[5:]
        if len(msg) == 1:
            await message.answer('<code>!poc CVE-2023-46604</code>')
        else:
            get_poc(msg2)
            output_file = "poc.json"
            with open(output_file, "r") as file:
                data = json.load(file)
            lst = []
            for item in data["pocs"]:
                lst.append('<b>' + item['name'] + '</b>' + '\n' + item['html_url'] + '\n' + '-' * 20 + '\n')

                await message.answer(f'{"".join(lst)}', disable_web_page_preview=True)
    except Exception as e:
        await message.answer(str(e))
        ic()
        ic(e)
        logging.error(e)
