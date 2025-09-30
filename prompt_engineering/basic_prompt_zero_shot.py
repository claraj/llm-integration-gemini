from google import genai 
import os 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)


response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""We are a company selling logging and monitoring products.
    What are good promotional products to give away at our conference booth at PyCon?"""   
)

print(response.text)




