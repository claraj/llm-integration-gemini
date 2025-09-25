from google import genai 
from google.genai.types import GenerateContentConfig 

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents='Suggest 5 business names for a barber. Just reply with the names',
    config=GenerateContentConfig(
        temperature=0,
        top_p=0)
)

print('Most probable names\n', response.text)


response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents='Suggest 5 business names for a barber. Just reply with the names',
    config=GenerateContentConfig(
        temperature=1,  
        top_p=0.5)   
)

print('\nCreative names\n', response.text)


response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents='Suggest 5 business names for a barber. Just reply with the names',
    config=GenerateContentConfig(
        temperature=2,  
        top_p=1)  
)

print('\nVery creative and random names\n', response.text)


