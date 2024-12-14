import openai
import os
# Replace with your OpenAI API key
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

try:
    response = openai.Embedding.create(
        input=["Test embedding generation"],
        engine="text-embedding-ada-002"
    )
    print("Embedding generated successfully:", response['data'][0]['embedding'])
except openai.error.OpenAIError as e:
    print("Error:", e)