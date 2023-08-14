from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder
from icecream import ic
from app.config import cfg

router: Router = Router()


@router.message(F.text.in_(cfg.all_commands['links_cmds']))
async def links_buttons(message: Message):
    try:
        builder = InlineKeyboardBuilder()
        builder.add(InlineKeyboardButton(
            text="🎩 Канал",
            url='https://t.me/pt_soft')
        )
        builder.add(InlineKeyboardButton(
            text="🎩 Группа",
            url="https://t.me/pt_hat")
        )
        builder.add(InlineKeyboardButton(
            text="💻 Get Kali Linux",
            url="https://www.kali.org/get-kali/")
        )
        builder.add(InlineKeyboardButton(
            text="🐈‍ HashCat examples",
            url="https://hashcat.net/wiki/doku.php?id=example_hashes")
        )
        builder.add(InlineKeyboardButton(
            text="🐧 Linux PrivEsc (gtfo)",
            url="https://gtfobins.github.io/")
        )
        builder.add(InlineKeyboardButton(
            text="🖥 Windows enum cheatsheet",
            url="https://wadcoms.github.io/")
        )
        builder.add(InlineKeyboardButton(
            text="♻️ cURL converter",
            url="https://curlconverter.com/")
        )
        builder.add(InlineKeyboardButton(
            text="🤖 File IDs bot",
            url="https://t.me/File_IDs_bot")
        )

        builder.adjust(2)
        await message.answer(
            "Ссылки:",
            reply_markup=builder.as_markup()
        )
    except Exception as e:
        ic(e)
        await message.answer(f'{e}')
