import asyncio

from aiogram import Dispatcher, Bot, F
from aiogram.filters import Command
from aiogram.types import Message

import AI
from config import config
from keyboard.menu import main_menu_command

API_TOKEN = config.token
bot = Bot(token=API_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands='start'))
async def start(message: Message):
    await message.answer('Привет! Я шар предсказаний!')


@dp.message(Command(commands='help'))
async def help_command(message: Message):
    await message.answer('Ты пишешь вопрос, а я предсказываю его будущее')


@dp.message(F.text)
async def text_user(message: Message):
    otvets = AI.generate_answer()
    if otvets:
        await message.answer(otvets)


async def main():
    try:
        print('Bot Started')
        await dp.start_polling(bot)
        await bot.set_my_commands(main_menu_command)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        print('Bot stopped')
