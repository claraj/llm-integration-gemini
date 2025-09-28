from google import genai
from google.genai import types
import os 
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
import pandas 
from google.genai.types import GenerateContentConfig
import rich 
from rich.markdown import Markdown

# This needs a billing account to work. See D2L for student credit - DO NOT USE YOUR OWN CREDIT CARD! 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')
client = genai.Client(api_key=GOOGLE_API_KEY)

chat = client.chats.create(
    model='gemini-2.5-flash',
    config=GenerateContentConfig(
        system_instruction="""You are Betty, the chatbot representative for Zoomies! athletic clothing company
        You are a young, active, on-trend chatbot. You are always upbeat, positive and happy.
        You can only chat about Zoomies! clothes and not anything else, and never talk about any other clothing companies
        You are here to help customers find the perfect fit in our clothes.
        Do not offer refunds or exchanges to customers. 
        If a customer asks about a refund, refer to our policy that we do not offer refunds or exchanges by post, 
        customers have to visit a retail store."""
        )
    )

clothing_document_file = 'fitness_clothing_descriptions.csv'

ids = []   # Unique ID for each document. We'll use the style code 
documents = []  # The main text about each document. Using the data from the description column 

with open(clothing_document_file, 'r') as file:
    clothing_data = pandas.read_csv(file)
    ids = list(clothing_data.style_code)
    documents = list(clothing_data.description)
  

class GeminiEmbeddingFunction(EmbeddingFunction):
    # Specify whether to generate embeddings for documents; or query mode, for finding relevant documents
    document_mode = True

    def __call__(self, input: Documents) -> Embeddings:
        if self.document_mode:
            embedding_task = 'retrieval_document'
        else:
            embedding_task = 'retrieval_query'

        response = client.models.embed_content(
            model='models/text-embedding-004',
            contents=input,
            config=types.EmbedContentConfig(
                task_type=embedding_task,
            ),
        )
        return [e.values for e in response.embeddings]
    

DB_NAME = 'zoomies_clothes'

embed_fn = GeminiEmbeddingFunction()
embed_fn.document_mode = True  # For generating embeddings as we load the documents 

chroma_client = chromadb.PersistentClient()
db = chroma_client.get_or_create_collection(name=DB_NAME, embedding_function=embed_fn)

db.upsert(   # add new if they don't exist, don't overwrite if they do. 
   ids=ids,
   documents=documents
)

# Switch to query mode when searching DB
embed_fn.document_mode = False

# Start chatbot 

print('This is Betty with Zoomies! How can I help you?')
while True:
  
    user_query = input('✨> ')

    # Search the Chroma DB using the specified query from the customer.
    # example query = 'what top goes with the core edge pants?'

    number_of_results = 5   # How many documents to retrieve 

    result = db.query(query_texts=[user_query], n_results=number_of_results)
    [all_items] = result['documents']

    print(all_items)

    # The LLM will understand the structure of the prompt better if the customer query, and the relevant documents, are on one line each. 
    query_oneline = user_query.replace('\n', ' ')

    prompt = f"""The customer has the following question:

    QUESTION: {query_oneline}

    Here is information from the items in our clothing database that may help answer the customer's question,
    """

    # Add the retrieved documents to the prompt.
    for passage in all_items:
        passage_oneline = passage.replace('\n', ' ')
        prompt += f'ITEM: {passage_oneline}\n'

    print(prompt)

    # Send message to LLM including retreived documents 
    response = chat.send_message(prompt)
    rich.print(Markdown(response.text))