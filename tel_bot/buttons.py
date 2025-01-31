"""Используемые в проекте кнопки"""

from pyrogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from pyrogram import emoji

back_button = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
help_button = KeyboardButton(f'{emoji.WHITE_QUESTION_MARK} Помощь')
new_task_button = KeyboardButton(f'{emoji.FOUNTAIN_PEN} Список дел')



web_app_address = WebAppInfo(url='https://faf953cd-e981-404e-a450-131fda6553a9-00-w9petonsr32k.sisko.replit.dev/')
web_app_button = InlineKeyboardButton(f'{emoji.SPIDER_WEB} Переход в веб-приложение',
                                      web_app=web_app_address)
