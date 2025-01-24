from logging import basicConfig, getLogger, INFO

from pyrogram import Client, filters
from pyrogram.types import Message

from config import API_ID, API_HASH, BOT_TOKEN
from keyboards import main_keyboard, setting_keyboard, web_keyboard_inline
from buttons import help_button, back_button, new_task_button
from custom_filters import button_filter

basicConfig(level=INFO, format="%(asctime)s : %(levelname)s : %(message)s")
logger = getLogger(__name__)

bot = Client(
    api_id=API_ID,
    bot_token=BOT_TOKEN,
    api_hash=API_HASH,
    name="GS_tg_bot_",
)


@bot.on_message(filters=filters.command("start") | button_filter(back_button))
async def start_command(client: Client, message: Message):
    logger.info(f"Bot started by {message.from_user.id}")
    await message.reply(f"Привет, {message.from_user.first_name}! Я бот, который умеет составлять список дел. \n"
                        f"Нажми на кнопку '{help_button.text}' для получения списка команд.",
                        reply_markup=main_keyboard)


@bot.on_message(filters=filters.command("help") | button_filter(help_button))
async def help_command(client: Client, message: Message):
    logger.info(f"Функция ' help_command' вызвана пользователем {message.from_user.id}")
    commands = await client.get_bot_commands()
    text_commands = "Список доступных команд \n"
    for command in commands:
        text_commands += f"/{command.command} - {command.description} \n"
    await message.reply(text_commands, reply_markup=setting_keyboard)


@bot.on_message(filters=filters.command('task') | button_filter(new_task_button))
async def new_task(client: Client, message: Message):
    logger.info(f"Функция ' new_task' вызвана пользователем {message.from_user.id}")
    await message.reply(f"Открыть web приложение", reply_markup=web_keyboard_inline)


@bot.on_message()
async def unknown_message(client: Client, message: Message):
    await message.reply(f"Неизвестная команда \n Введите '/help' для получения списка доступных команд")


if __name__ == "__main__":
    bot.run()
