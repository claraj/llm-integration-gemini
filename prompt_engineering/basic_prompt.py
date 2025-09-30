from google import genai 
import os 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents='Why is the sky blue?'
)

print(response.text)


