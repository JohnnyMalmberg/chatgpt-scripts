import sys
import openai
import os

model = 'gpt-3.5-turbo'

query = ' '.join(sys.argv[1:])

comp = openai.ChatCompletion.create(model=model, messages=[{"role":"user","content":query}])

response = comp["choices"][0]["message"]["content"].strip()

print(f'ChatGPT:\n\n{response}\n')

