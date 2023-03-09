import openai
import os
openai.api_key = os.getenv('OPENAI_API_KEY', 'default')

msg = [{"role": "system", "content": "あなたは賢いAIです。"}]
while True:
    prompt = input("> ").strip()
    if prompt in ["quit", "exit"]:
        break
    msg.append({"role": "user", "content": prompt})
    res = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=msg)
    ans = res["choices"][0]["message"]["content"].strip()
    print(ans)
    msg.append({"role": "assistant", "content": ans})
    if res["usage"]["total_tokens"] > 3000:
        msg.pop(1)