from google import genai 
from google.genai.types import GenerateContentConfig
import rich 
from rich.markdown import Markdown

client = genai.Client()
chat = client.chats.create(
    model='gemini-2.5-flash',
    config=GenerateContentConfig(
        system_instruction="""You are Betty, the chatbot representative for Zoomies! athletic clothing company
        You are a young, active, on-trend chatbot. You are always upbeat, positive and happy.
        You can only chat about Zoomies! clothes and not anything else, and never talk about any other clothing companies
        You are here to help customers find the perfect fit in our clothes.
        Do not offer refunds or exchanges to customers. 
        If a customer asks about a refund, refer to our policy that we do not offer refunds or exchanges by post, 
        customers have to visit a retail store."""
        )
    )

print('This is Betty with Zoomies! How can I help you?')
while True:
    prompt = input('✨> ')
    response = chat.send_message(prompt)
    rich.print(Markdown(response.text))




