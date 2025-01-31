from pyrogram import filters
from pyrogram.types import Message, KeyboardButton

def button_filter(button: KeyboardButton):
    async def func (_, __, message: Message):
        return message.text == button.text

    return filters.create(func, "ButtonFilter", button=button)