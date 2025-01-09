from pyrogram.types import ReplyKeyboardMarkup
from buttons import help_button, new_task_button, back_button, tasks_button

main_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [new_task_button, tasks_button],
        [help_button]
    ], resize_keyboard=True)

setting_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [back_button]
    ], resize_keyboard=True)
