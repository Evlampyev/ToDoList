"""Используемые в проекте кнопки"""

from pyrogram.types import KeyboardButton

from pyrogram import emoji

back_button = KeyboardButton(f'{emoji.BACK_ARROW} Назад')
help_button = KeyboardButton(f'{emoji.WHITE_QUESTION_MARK} Помощь')
new_task_button = KeyboardButton(f'{emoji.FOUNTAIN_PEN} Добавить задачу')
tasks_button = KeyboardButton(f'{emoji.NEWSPAPER} Список задач')

