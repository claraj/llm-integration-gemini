from google import genai
from google.genai import types
import os 
import chromadb
from chromadb import Documents, EmbeddingFunction, Embeddings
import pandas 

# This needs a billing account to work. See D2L for student credit - DO NOT USE YOUR OWN CREDIT CARD! 

GOOGLE_API_KEY = os.environ.get('GEMINI_API_KEY')

client = genai.Client(api_key=GOOGLE_API_KEY)

clothing_document_file = 'fitness_clothing_descriptions.csv'

ids = []   # Unique ID for each document. We'll use the style code 
documents = []  # The main text about each document. Using the data from the description column 

with open(clothing_document_file, 'r') as file:
    clothing_data = pandas.read_csv(file)
    ids = list(clothing_data.style_code)
    documents = list(clothing_data.description)
  

class GeminiEmbeddingFunction(EmbeddingFunction):
    # Specify whether to generate embeddings for documents, or for running queries
    document_mode = True

    # @retry.Retry(predicate=is_retriable)
    def __call__(self, input: Documents) -> Embeddings:
        if self.document_mode:
            embedding_task = "retrieval_document"
        else:
            embedding_task = "retrieval_query"

        response = client.models.embed_content(
            model="models/text-embedding-004",
            contents=input,
            config=types.EmbedContentConfig(
                task_type=embedding_task,
            ),
        )
        return [e.values for e in response.embeddings]
    

DB_NAME = "zoomies_clothes"

embed_fn = GeminiEmbeddingFunction()
embed_fn.document_mode = True  # For generating embeddings 

chroma_client = chromadb.PersistentClient()
db = chroma_client.get_or_create_collection(name=DB_NAME, embedding_function=embed_fn)

db.add(
   ids=ids,
   documents=documents
)


# Switch to query mode when searching DB
embed_fn.document_mode = False

# Search the Chroma DB using the specified query from the customer.
query = "what sweatpants are good for winter"

result = db.query(query_texts=[query], n_results=5)
[all_items] = result["documents"]

print(all_items)


query_oneline = query.replace("\n", " ")


prompt = f"""You are a helpful assistant called Betty who works for Zoomies! Clothing. The customer has the following question:

QUESTION: {query_oneline}

Here is information from the items in the clothing database that may help answer the customer's question,

"""

# Add the retrieved documents to the prompt.
for passage in all_items:
    passage_oneline = passage.replace("\n", " ")
    prompt += f"ITEM: {passage_oneline}\n"

print(prompt)


answer = client.models.generate_content(
    model="gemini-2.0-flash",
    contents=prompt
    # todo - add system instructions 
    )

print(answer.text)