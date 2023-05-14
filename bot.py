from peewee import *
from telebot import TeleBot
app = TeleBot("bot")
from initialDatabase import *

def print_hi(name):
    print(f'Hi, {name}')

@app.route('(?!/).+')
def message_help(context):
    chat_id = context["chat"]["id"]
    text = context['text']
    first_name = User["first_name"]
    last_name = User["last_name"]
    username = User["username"]
    language_code = User["language_code"]
    roleid = User["roleid"]
    if __name__ == '__main__':
        print_hi('PyCharm')
        app.send_message(chat_id, text)
    if  User["id"] == chat_id:
        print("Такой пользователь уже существует.")
    else:
        User.create(id= chat_id, is_bot= True, first_name= first_name, last_name= last_name, username= username, language_code =language_code, roleid= roleid)
with open("bot.auth", 'r') as file:
    token = file.readline()
    app.config['api_key'] = token

app.poll(debug=True)