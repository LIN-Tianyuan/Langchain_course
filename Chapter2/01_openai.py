# pip install python-dotenv 
from openai import OpenAI 
from dotenv import load_dotenv 

load_dotenv() # Load .env by default

client = OpenAI()

response = client.responses.create(model="gpt-5.6", input="Write a short bedtime story about a unicorn.")

print(response.output_text)