from peewee import *
from initialDatabase import *
from telebot_router import TeleBot
from cache import *


app = TeleBot("bot")


@app.route('(?!/).+')
def message_help(context):
    chat_id = context["chat"]["id"]
    text = context['text']
    app.send_message(chat_id, text)

    user = GetInstance(chat_id)
    if user == None:
        first_name = context['from']["first_name"]
        last_name = context['from']["last_name"]
        username = context['from']["username"]
        language_code = context['from']["language_code"]

        user = User.create(chat_id= chat_id, is_bot= True, first_name= first_name, last_name= last_name, username= username, language_code =language_code, roleid= 2)
        user.save()

with open("bot.auth", 'r') as file:
    token = file.readline()
    app.config['api_key'] = token

app.poll(debug=True)
con.close()