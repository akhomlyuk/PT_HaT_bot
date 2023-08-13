import asyncio
import logging
import os
from aiogram import Dispatcher, types
import app.config.cfg as cfg
from app.handlers import help, useful, wiki, base_tools, hex_tools, hash_tools_handler, free_gpt, sqli_tools, ssti, searchsploit, check_port
from app.keyboards import kb_menu, kb_links
from icecream import ic

os.makedirs('logs', exist_ok=True)

bot = cfg.bot
dp = Dispatcher()

# Подключаем роутеры
dp.include_router(help.router)
dp.include_router(useful.router)
dp.include_router(kb_menu.router)
dp.include_router(kb_links.router)
dp.include_router(wiki.router)
dp.include_router(base_tools.router)
dp.include_router(hex_tools.router)
dp.include_router(hash_tools_handler.router)
dp.include_router(free_gpt.router)
dp.include_router(sqli_tools.router)
dp.include_router(ssti.router)
dp.include_router(searchsploit.router)
dp.include_router(check_port.router)


@dp.errors()
async def errors_handler(update: types.Update, exception: Exception):
    logging.error(f'Ошибка при обработке запроса {update}: {exception}')


async def main():
    try:
        await dp.start_polling(bot)
    except (KeyboardInterrupt, SystemExit) as e:
        logging.info("Bot stopped")
        ic(e)
    finally:
        await bot.session.close()


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, filename='logs/bot.log',
                        format="%(filename)s:%(lineno)d #%(levelname)-8s" "[%(asctime)s] - %(name)s - %(message)s")
    logging.info('Bot starting...')
    asyncio.run(main())
