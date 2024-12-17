import asyncio

from src.handlers.handlers import router
from keys.token import key

from aiogram import Bot, Dispatcher



async def main():
    bot = Bot(token=key)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)



if __name__ == '__main__':
    try:
        asyncio.run(main())
    except Exception as ext:
        print(ext)