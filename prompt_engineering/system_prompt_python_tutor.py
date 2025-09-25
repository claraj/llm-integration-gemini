from google import genai 
from google.genai.types import GenerateContentConfig

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""Write a program to calculate the area of a circle""",
    config=GenerateContentConfig(
        system_instruction="""You are a helpful programming tutor for beginning Java programming students. 
        You can explain concepts and answer questions about coding. But if the user asks for code, don't 
        generate it, but ask them questions and explain concepts to help them understand how to write
        the code themselves. Be positive and encouraging at all times"""
        )
    )

print(response.text)


