from google import genai 
import rich 
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(model='gemini-2.5-flash')

print('Welcome to the Chatbot! Please enter your prompt below:')
while True:
    prompt = input('> ')
    response = chat.send_message(prompt)
    rich.print(Markdown(response.text))
