from google import genai 
from google.genai import types
from pydantic import BaseModel

class Product(BaseModel):
    name: str 
    color: str 
    fruit_or_veg: str 

client = genai.Client()

with open('fruits-and-vegetables.jpg', 'rb') as f:
    image_bytes = f.read()

response = client.models.generate_content(
  model='gemini-2.5-flash',
  contents=[
    types.Part.from_bytes(
      data=image_bytes,
      mime_type='image/jpeg',
    ),
    'What produce is in this picture?'
  ],
  config=types.GenerateContentConfig(
      system_instruction="""List the name of the product, the typical color, '
      and "fruit" for fruits and "vegetable" for vegetable """,
      response_mime_type='application/json',
      response_schema=list[Product]
      
  )
)

print(response.text)

