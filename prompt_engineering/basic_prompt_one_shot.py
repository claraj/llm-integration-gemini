from google import genai 

client = genai.Client()

response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents="""We are a company selling logging and monitoring products.
    What are good promotional products to give away at our conference booth at PyCon? 
    Last year we gave away tote bags and they were very popular."""   
)

print(response.text)





