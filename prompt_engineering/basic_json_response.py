from google import genai 
from google.genai.types import GenerateContentConfig

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""I have cheese, broccoli, 
    and leftover chicken. Suggest a recipe""",
    config=GenerateContentConfig(
        response_mime_type='application/json'
        )
    )

print(response.text)


