from aiogram import executor
import logging
from bot import dp

logging.basicConfig(level=logging.INFO)


def main():
    from handlers import handler

    executor.start_polling(dp, skip_updates=True)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
