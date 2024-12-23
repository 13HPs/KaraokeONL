import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()  # Load environment variables from.env file

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY'),
)
response = client.embeddings.create(
    input="test string",
    model="text-embedding-3-small",
)

print(response.data[0].embedding)