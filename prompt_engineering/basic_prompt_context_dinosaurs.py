from google import genai 
import os 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)


response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""I need to explain to my 5-year-old why the sky is blue. 
    They love dinosaurs, can you use a dinosaur analogy?"""
)

print(response.text)




