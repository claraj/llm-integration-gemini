from google import genai 
from google.genai.types import GenerateContentConfig
import os 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""I have cheese, broccoli, 
    and leftover chicken. Suggest a recipe""",
    config=GenerateContentConfig(
        response_mime_type='application/json'
        )
    )

print(response.text)


