from google import genai 

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""I need to explain to my 5-year-old why the sky is blue. 
    They love dinosaurs, can you use a dinosaur analogy?"""
)

print(response.text)




