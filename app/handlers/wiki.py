from aiogram import Router, F, html
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from icecream import ic
import wikipedia

router: Router = Router()


@router.message(F.text.startswith(cfg.all_commands['wiki_cmds']))
async def rht_art(message: Message):
    wikipedia.set_lang("ru")
    try:
        msg = message.text
        if len(msg.split()) < 2:
            await message.answer(f'Пример: <code>!wiki linux</code>')
        else:
            w = wikipedia.page(message.text[6:], auto_suggest=True)
            wiki_page = wikipedia.summary(message.text[6:], sentences=4, auto_suggest=True)
            wiki_url = w.url
            await message.answer(f'{wiki_page}\n\n{wiki_url}', disable_web_page_preview=True)
    except wikipedia.exceptions.PageError as e:
        await message.answer('Страницы на русском не существует :(')
        logging.warning(e)
        ic(e)
