from aiogram import Router, F, html
from aiogram.types import Message, URLInputFile
import logging
import app.config.cfg as cfg
from app.config.cfg import bot
from app.helpers.revshell import generate_revshell
from app.helpers.jwt_decode import jwt_decode
from icecream import ic
import os
import json

router: Router = Router()


@router.message(F.text.in_(cfg.all_commands['id_cmds']))
async def show_menu(message: Message):
    try:
        await message.answer(f'<b>ID:</b> <code>{message.from_user.id}</code> Premium: <b>{message.from_user.is_premium}</b>')
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')


@router.message(F.text.in_(cfg.all_commands['invite_cmds']))
async def create_invite(message: Message):
    try:
        invite = await message.bot.create_chat_invite_link(message.chat.id)
        await message.answer(f'{invite.invite_link}')
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')


@router.message(F.text.in_(cfg.all_commands['python_cmds']))
async def python_onepic(message: Message):
    try:
        photo = URLInputFile('https://raw.githubusercontent.com/coreb1t/awesome-pentest-cheat-sheets/master/docs/python-3-in-one-pic.png',
                             bot=bot, filename='python3_onepic.png')
        await message.answer_document(photo)
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')


@router.message(F.text.in_(cfg.all_commands['lin_cmds']))
async def linux_onepic(message: Message):
    try:
        photo = URLInputFile('https://raw.githubusercontent.com/coreb1t/awesome-pentest-cheat-sheets/master/docs/python-3-in-one-pic.png',
                             bot=bot, filename='linux_commands.jpg')
        await message.answer_document(photo)
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')


@router.message(F.text.in_(cfg.all_commands['commands_cmds']))
async def show_commands(message: Message):
    try:
        await message.answer(f'{cfg.bot_commands}')
    except Exception as e:
        ic(e)


# Декодирование header и payload JWT
@router.message(F.text.startswith(cfg.all_commands['jwt_cmds']))
async def send_decode_jwt(message: Message):
    try:
        jwt = message.text.split()
        ic(jwt)
        ic()
        if len(jwt) != 2:
            await message.answer(
                f'Пример:\n<code>!jwt eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWUsImlhdCI6MTY5MTAxMjU3MSwiZXhwIjoxNjkxMDE2MTcxfQ.BNM4pLUB6wYlnXC0NvHiShDIM6KtIk81prLW8VBCZ88</code>')
        else:
            await message.answer(f'<b>Header:</b>\n<code>{jwt_decode(jwt[1])[0]}</code>\n\n'
                                 f'<b>Payload:</b>\n<code>{jwt_decode(jwt[1])[1]}</code>')
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'Не валидный JWT')


# Вывод всех команд бота
@router.message(F.text.in_(cfg.all_commands['cmds_cmds']))
async def show_all_commands(message: Message):
    try:
        commands = '\t'.join([str('<code>' + v + '</code>') for v in cfg.all_commands.values()])
        await message.answer(f'{commands}')
    except Exception as e:
        logging.warning(e)
        ic(e)
        await message.answer(f'{e}')


# Отправка строки с последующей генерацией и выводом реверс шелла
@router.message(F.text.startswith(cfg.all_commands['rev_cmds']))
async def send_rev_shell(message: Message):
    try:
        revs = ['php', 'bash', 'python', 'nc', 'socat', 'ruby', 'node']
        example = (f'Примеры команд:\n\n<code>!rev (nc,php,bash) 127.0.0.1 31337</code>\n<code>!rev 127.0.0.1 31337</code>\n\n'
                   f'<b>{" : ".join(str(s) for s in revs)}</b>')
        msg = message.text
        msg = msg.split(' ')
        if len(msg) == 3:
            await message.answer(f'<code>{html.quote(generate_revshell(msg[1], int(msg[2]), None))}</code>')
        elif len(msg) == 4:
            if msg[1] not in revs:
                await message.answer(f'{example}')
            else:
                match msg[1]:
                    case "php":
                        await message.answer(f'<code>{html.quote(generate_revshell(msg[2], int(msg[3]), revs[0]))}</code>')
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
        bot_obj = await bot.get_me()
        bot_id = bot_obj.id

        msg_obj = message.model_dump(mode='python')
        msg_obj_ex = message.model_dump(mode='python', exclude={'from_user', 'chat', 'date'})
        from_user = {}
        chat = {}
        data = {}
        for key, value in msg_obj_ex.items():
            if value is not None:
                data[key] = value
        for key, value in msg_obj['from_user'].items():
            if value is not None:
                from_user[key] = value
        for key, value in msg_obj['chat'].items():
            if value is not None:
                chat[key] = value
        json_fromuser = json.dumps(from_user, indent=2)
        json_chat = json.dumps(chat, indent=2)
        json_data = json.dumps(data, indent=2)

        for chat_member in message.new_chat_members:
            if chat_member.id == bot_id:
                logging.info(f'Бота добавили в группу: {message.chat.title, message.chat.id, message.chat.type}')
                await bot.send_message(539491282, text=f'<b>message_from_user</b>\n<code>{json_fromuser}</code>\n'
                                                       f'<b>message_chat</b>\n<code>{json_chat}</code>\n'
                                                       f'<b>message</b>\n<code>{json_data}</code>\n'
                                                       f'{await bot.get_chat(message.chat.id)}\n')
        new_member = message.new_chat_members[0]
        await cfg.bot.send_message(message.chat.id, f"Добро пожаловать в <b>{message.chat.title}</b> 🖖, @{new_member.username} ! 🎩")
        await cfg.bot.send_message(message.chat.id, f"{cfg.bot_commands}")
    except Exception as e:
        logging.error(f'{e}')
        ic(e)


# Автоматическое удаление системных сообщений
@router.message(F.left_chat_member)
async def on_user_left(message: Message):
    try:
        await message.delete()
    except Exception as e:
        ic()
        ic(e)


@router.message(F.new_chat_photo)
async def on_new_photo(message: Message):
    try:
        await message.delete()
    except Exception as e:
        ic()
        ic(e)


@router.message(F.delete_chat_photo)
async def on_delete_photo(message: Message):
    try:
        await message.delete()
    except Exception as e:
        ic()
        ic(e)


@router.message(F.text.in_('!uptime'))
async def uptime_info(message: Message):
    t = os.popen('uptime -p').read()[:-1]
    await message.answer(f'{t}')
