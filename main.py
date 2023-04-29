#This is an Open AI Chatbot (GPT-3.5). Which can answer any question. 🤖

#You can ask anything as you wish.😀

# ⚠️ It may not work if the answer is huge! So, ask any simple and short questions (Example: what is cat?) 

import os
os.system('pip install -qq openai')

ask = input()

import openai

openai.api_key = "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"
completion = openai.ChatCompletion.create(model="gpt-3.5-turbo", messages=[{"role": "user", "content": f"{ask}"}])


print(f"""{ask}

{completion.choices[0].message.content}""")
