import openai
from telebot_router import TeleBot

openai.api_key = "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"
model_engine = "text-davinci-003"
app = TeleBot("bot")

@app.route('(?!/).+')
def message_help(context):
    text = context["text"]
    chat_id = context["chat"]["id"]
    prompt = f"{text}"
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    answer = response.choices[0].text
    app.send_message(chat_id, answer)
app.config['api_key'] = "5796515330:AAGwJExHhRvtEG_GtEyQ1tosguWrJY4CcIk"
app.poll(debug=True)
