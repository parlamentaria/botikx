import os
import asyncio
from aiogram import Bot, Dispatcher, types

TOKEN = os.getenv("7530716464:AAEEnqZLchL5GGrNYOAocqNpi8-8loaaSbY")  # Загружаем токен из переменной окружения
bot = Bot(token=TOKEN)
dp = Dispatcher()

@dp.message()
async def echo(message: types.Message):
    await message.answer(message.text)

async def main():
    print("Бот запущен...")
    await dp.start_polling(bot)

if name == "main":
    asyncio.run(main())
