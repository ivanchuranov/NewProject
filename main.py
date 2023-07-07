from Models.initialDatabase import *
from telebot_router import TeleBot
from Services.UserService import UserService
from Services.ProceduresService import ProceduresService
from Services.SpecialOffersService import SpecialOffersService


app = TeleBot("bot")

@app.route('(?!/).+')
def message_help(context):
    user = UserService.GetUserByContext(context)
    text = context['text']
    app.send_message(user.chat_id, text)

@app.route('/procedures')
def procedures_handler(context):
    user = UserService.GetUserByContext(context)
    result = ProceduresService.GetProceduresText()
    app.send_message(user.chat_id, result)

@app.route('/specials')
def specials_handler(context):
    user = UserService.GetUserByContext(context)

    try:
        id = int(context['text'].split(" ")[1])

        result = SpecialOffersService.GetSpecialOfferText(id)
    except:
        result = "Такого идентификатора не существует."

    app.send_message(user.chat_id, result)


with open("bot.auth", 'r') as file:
    token = file.readline()
    app.config['api_key'] = token

app.poll(debug=True)
con.close()