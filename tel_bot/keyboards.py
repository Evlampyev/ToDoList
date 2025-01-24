"""Используемые в проекты наборы клавиатур"""
from pyrogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup
from buttons import help_button, new_task_button, back_button, web_app_button

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [new_task_button, help_button]
    ], resize_keyboard=True)

setting_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [back_button]
    ], resize_keyboard=True)

web_keyboard_inline = InlineKeyboardMarkup(
    inline_keyboard=[
        [web_app_button],
    ]

)
