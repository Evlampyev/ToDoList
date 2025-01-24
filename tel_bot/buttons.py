"""Используемые в проекте кнопки"""

from pyrogram.types import KeyboardButton, InlineKeyboardButton, InlineKeyboardMarkup, WebAppInfo

from pyrogram import emoji

back_button = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
help_button = KeyboardButton(f'{emoji.WHITE_QUESTION_MARK} Помощь')
new_task_button = KeyboardButton(f'{emoji.FOUNTAIN_PEN} Список дел')



web_app_address = WebAppInfo(url='https://yandex.ru/all')
web_app_button = InlineKeyboardButton(f'{emoji.SPIDER_WEB} Переход в веб-приложение',
                                      web_app=web_app_address)
