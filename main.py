from telebot import TeleBot
from peewee import *

app = TeleBot("bot")

@app.route('(?!/).+')
def message_help(message):
    msg = "(?!/).+"
    app.send_message(msg)


app.config['api_key'] = "5796515330:AAGwJExHhRvtEG_GtEyQ1tosguWrJY4CcIk"
app.poll(debug=True)
