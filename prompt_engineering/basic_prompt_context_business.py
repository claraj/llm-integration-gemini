from google import genai 

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""We run a yoga studio near the University of Minneapolis. 
    Our clients are mostly college students because they can walk to the studio.
    We have been very quiet during the summer. Can you suggest some strategies to get more 
    customers during the summer months?"""
)

print(response.text)

