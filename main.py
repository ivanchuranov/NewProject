from telebot_router import TeleBot
from peewee import *

app = TeleBot("bot")


@app.route('(?!/).+')
def message_help(context):
    chat_id = context["chat"]["id"]
    text = context['text']

    app.send_message(chat_id,text)


with open("bot.auth", 'r') as file:
    token = file.readline()
    app.config['api_key'] = token

app.poll(debug=True)