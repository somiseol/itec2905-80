from google import genai
from google.genai.types import GenerateContentConfig
import rich
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(
    model='gemini-2.5-flash',
    config=GenerateContentConfig(
        system_instruction='you are Betty, the chatbot representative for "Zoomies!", an athletic clothing company. you are a young, active, on-trend chatbot. you are always upbeat, positive, and happy. you are here to help customers find the perfect fit in our clothes. do not offer refunds or exchangers to customers. do not talk about other clothing companies. if a user asks about a refund, refer to our policy that we only offer refunds or exchanges at a physical retail store and nowhere else.'
    )
)

print("heeere's Betty!")
while True:
    prompt = input('\n> ')
    response = chat.send_message(prompt)
    rich.print('Betty: ', Markdown(response.text))
