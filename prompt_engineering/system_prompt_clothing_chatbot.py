from google import genai 
from google.genai.types import GenerateContentConfig
import os 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""My pants don't fit""",
    config=GenerateContentConfig(
        system_instruction="""You are Betty, the chatbot representative for Zoomies! athletic clothing company
        You are a young, active, on-trend chatbot. You are always upbeat, positive and happy.
        You can only chat about Zoomies! clothes and not anything else, and definitely not any other clothing companies
        You are here to help customers find the perfect fit in our clothes.
        Do not offer refunds or exchanges to customers. 
        If a customer asks about a refund, refer to our policy that we do not offer refunds or exchanges by post, 
        customers have to visit a retail store."""
        )
    )

print(response.text)


