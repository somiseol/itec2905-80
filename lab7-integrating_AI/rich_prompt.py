from google import genai
import rich
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash')

print('welcome to the chatbot. please enter your prompt:')
while True:
    prompt = input('> ')
    response = chat.send_message(prompt)
    rich.print(Markdown(response.text))
