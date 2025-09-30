import os 
import sys 
from google import genai 
from google.genai.types import GenerateContentConfig
import rich 
from rich.markdown import Markdown

import os 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)

system_instruction_file_path = os.path.join('system_instructions', 'clothing_chatbot.txt')

try: 
    with open(system_instruction_file_path, 'r') as file:
        system_instruction = file.read()
except Exception as e:
    print('System instructions not found')
    sys.exit()

chat = client.chats.create(
    model='gemini-2.5-flash',
    config=GenerateContentConfig(
        system_instruction=system_instruction
        )
    )

print('This is Betty with Zoomies! How can I help you?')
while True:
    prompt = input('✨> ')
    response = chat.send_message(prompt)
    rich.print(Markdown(response.text))




