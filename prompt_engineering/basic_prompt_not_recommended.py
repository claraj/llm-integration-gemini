from google import genai 

client = genai.Client()

# These types of question are not recommended
# There are better ways to perform these types of task 
# For example, using news API. The AI is probably out of date

# response = client.models.generate_content(
#     model='gemini-2.5-flash', 
#     contents='what are todays news headlines?'
# )

# print(response.text)

# All AI models have a cut off date beyond which they don't have any knowledge.
response = client.models.generate_content(
    model='gemini-2.5-flash', 
    contents='Who is the uk deputy prime minister?'      
)

# In September 2025 it responded with Oliver Dowden, who was replaced in July 2024. 
print(response.text)


# We can solve this problem with code 
# response = client.models.generate_content(
#     model='gemini-2.5-flash', 
#     contents='Sort this array [5, 6, 100, 1, 3, 0, -1, 45, 22]'
# )

# print(response.text)


