import logging
import requests
from aiogram import *

bot = Bot("Токен")
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

@dp.message_handler(commands="start")
async def start(message = types.Message):
    await message.answer("👋 Я чат-бот.\nОтправь ссобщние чтобы начать")


@dp.message_handler()
async def chat_bot(message = types.Message):
    try:
        json = requests.post('https://xu.su/api/send', data = {"uid":'',"bot":'Тян',"text":f'{message.text}'}).json()
    except:
        return await message.answer("❌ **API** Не отвечает.")    



    await message.answer(json['text']) 

            

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)
