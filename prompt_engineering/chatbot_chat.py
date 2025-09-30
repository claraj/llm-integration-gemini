from google import genai 
import rich 
from rich.markdown import Markdown
import os 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)


chat = client.chats.create(model='gemini-2.5-flash')

print('Welcome to the Chatbot! Please enter your prompt below:')
while True:
    prompt = input('> ')
    response = chat.send_message(prompt)
    rich.print(Markdown(response.text))
