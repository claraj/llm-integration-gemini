from google import genai 
import os 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)


response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""We run a yoga studio near the University of Minneapolis. 
    Our clients are mostly college students because they can walk to the studio.
    We have been very quiet during the summer. Can you suggest some strategies to get more 
    customers during the summer months?"""
)

print(response.text)

