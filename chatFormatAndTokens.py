import os
import openai
from dotenv import load_dotenv, find_dotenv

# Load environment variables
load_dotenv(find_dotenv())

# Get OpenAI API key
api_key = os.getenv('OPENAI_API_KEY')
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set in environment variables")

openai.api_key = api_key

def get_completion(prompt, model="gpt-4"):
    try:
        messages = [{"role": "user", "content": prompt}]
        response = openai.ChatCompletion.create(
            model=model,
            messages=messages,
        )
        return response.choices[0].message["content"]
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

response = get_completion("What is the capital of France?")
print(response)
