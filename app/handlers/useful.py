from aiogram import Router, F, html
from aiogram.types import Message
import logging
import app.config.cfg as cfg
from app.helpers.revshell import generate_revshell
from icecream import ic

router: Router = Router()
id_commands = ['!id']
cmds_commands = ['!cmds']


@router.message(F.text.in_(id_commands))
async def show_menu(message: Message):
    try:
        await message.answer(f'<b>ID:</b> <code>{message.from_user.id}</code>')
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')


@router.message(F.text.in_(cmds_commands))
async def show_menu(message: Message):
    try:
        await message.answer(f'{cfg.bot_commands}')
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')


# Отправка строки с последующей генерацией реверс шелла
@router.message(F.text.startswith('!rev'))
async def send_rev_shell(message: Message):
    try:
        revs = ['php', 'bash', 'python', 'nc', 'socat', 'ruby', 'node']
        example = (f'<code>!rev (nc,php,bash) 127.0.0.1 31337</code>\n<code>!rev 127.0.0.1 31337</code>\n\n'
                   f'<b>{" : ".join(str(s) for s in revs)}</b>')
        msg = message.text
        msg = msg.split(' ')
        ic(msg, len(msg))
        if len(msg) == 3:
            await message.answer(f'<code>{html.quote(generate_revshell(msg[1], int(msg[2]), None))}</code>')
        elif len(msg) == 4:
            if msg[1] not in revs:
                await message.answer(f'{example}')
            else:
                match msg[1]:
                    case "php":
                        await message.answer(f'<code>{html.quote(generate_revshell(msg[2], int(msg[3]), revs[0] ))}</code>')
                    case "bash":
                        await message.answer(f'<code>{html.quote(generate_revshell(msg[2], int(msg[3]), revs[1]))}</code>')
                    case 'python':
                        await message.answer(f'<code>{html.quote(generate_revshell(msg[2], int(msg[3]), revs[2]))}</code>')
                    case 'nc':
                        await message.answer(f'<code>{html.quote(generate_revshell(msg[2], int(msg[3]), revs[3]))}</code>')
                    case 'socat':
                        await message.answer(f'<code>{html.quote(generate_revshell(msg[2], int(msg[3]), revs[4]))}</code>')
                    case 'ruby':
                        await message.answer(f'<code>{html.quote(generate_revshell(msg[2], int(msg[3]), revs[5]))}</code>')
                    case 'node':
                        await message.answer(f'<code>{html.quote(generate_revshell(msg[2], int(msg[3]), revs[6]))}</code>')
        else:
            await message.answer(f'{example}')

    except Exception as e:
        logging.warning(e)
        ic(e)


# приветствие новых пользователей
@router.message(F.new_chat_members)
async def new_members_handler(message: Message):
    try:
        new_member = message.new_chat_members[0]
        await cfg.bot.send_message(message.chat.id, f"Добро пожаловать в HaT 🖖, @{new_member.username} ! 🎩🎩🎩")
    except Exception as e:
        logging.error(f'{e}')
        ic(e)
