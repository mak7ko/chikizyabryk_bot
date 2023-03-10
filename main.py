from aiogram import types
from aiogram.utils import executor
import datetime
from loader import bot, dp, logging
import handlers, filters

async def on_startup(x):
    logging.warning('Bot started')
    await bot.set_my_commands([
        types.BotCommand("do_not_click", "Не натискати!"),
        types.BotCommand("ban_me_please", "Чисте задоволення")
    ])

async def on_shutdown(x):
    logging.warning('Bot stopped')
    

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup, on_shutdown=on_shutdown)