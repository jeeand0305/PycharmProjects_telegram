from aiogram import types, Dispatcher
import string, json
from create_bot import dp

# @dp.message_handler()
async def echo_send(message: types.Message):
    if {i.lower().translate(str.maketrans
    ('', '', string.punctuation))
    for i in message.text.split(' ')}.intersection(set
    (json.load(open('cenz.json')))) != set():
       await message.reply("мат запрещен")
       await message.delete()

def register_message_hedler(dp : Dispatcher):
    dp.register_message_hedler \
        (echo_send)


