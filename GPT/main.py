import openai

openai.api_key = "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"
model_engine = "text-davinci-003"

while True:
    question = input("")
    prompt = f"{question}"

    # генерируем ответ
    completion = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=1024,
        temperature=0.5,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    answer = completion.choices[0].text
    print(answer)
    if question == "/stop":
        quit()
