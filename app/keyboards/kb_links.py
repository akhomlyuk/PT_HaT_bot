from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from icecream import ic

router: Router = Router()
menu_commands = ['!links']


@router.message(F.text.in_(menu_commands))
async def links_buttons(message: Message):
    try:
        builder = InlineKeyboardBuilder()
        builder.add(InlineKeyboardButton(
            text="Канал 🎩",
            url='https://t.me/pt_soft')
        )
        builder.add(InlineKeyboardButton(
            text="Группа 🎩",
            url="https://t.me/pt_hat")
        )

        builder.adjust(2)
        await message.answer(
            "Ссылки: ",
            reply_markup=builder.as_markup()
        )
    except Exception as e:
        ic(e)
        await message.answer(f'{e}')
