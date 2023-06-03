from Models.initialDatabase import *
from telebot_router import TeleBot
from Services.StorageService import StorageService


app = TeleBot("bot")

@app.route('(?!/).+')
def message_help(context):
    user = StorageService.GetUserByContext(context)
    text = context['text']
    app.send_message(user.chat_id, text)


with open("bot.auth", 'r') as file:
    token = file.readline()
    app.config['api_key'] = token

app.poll(debug=True)
con.close()