from aiogram import Router, F
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder
from icecream import ic

router: Router = Router()
menu_commands = ['!menu']


@router.message(F.text.in_(menu_commands))
async def menu_buttons(message: Message):
    try:
        builder = InlineKeyboardBuilder()
        builder.add(InlineKeyboardButton(
            text="Pentest HaT 🎩",
            callback_data="pt_hat_channel")
        )
        builder.add(InlineKeyboardButton(
            text="Группа 🎩",
            callback_data="pt_hat_group")
        )

        builder.adjust(2)
        await message.answer(
            "Меню:",
            reply_markup=builder.as_markup()
        )
    except Exception as e:
        ic(e)
        await message.answer(str(e))


@router.callback_query(F.data == 'pt_hat_channel')
async def send_channel_link(callback: CallbackQuery):
    await callback.message.answer('https://t.me/pt_soft')
    await callback.answer()


@router.callback_query(F.data == 'pt_hat_group')
async def send_group_link(callback: CallbackQuery):
    await callback.message.answer('https://t.me/pt_hat')
    await callback.answer()
