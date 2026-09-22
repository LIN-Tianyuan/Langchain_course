from pydantic import BaseModel, Field 
from langchain.chat_models import init_chat_model 
from langchain_core.output_parsers import JsonOutputParser 

from dotenv import load_dotenv 

load_dotenv() # Load .env by default

llm = init_chat_model( 
    model="gpt-5.4", 
    model_provider="openai", 
) 

# Define the structure you want the AI to return
class Prime(BaseModel): 
    prime: list[int] = Field(description="Prime Number") 
    count: list[int] = Field(description="The number of prime numbers less than that prime number") 

# JSON output structured according to the "Prime" Pydantic model.
json_parser = JsonOutputParser(pydantic_object=Prime) 
messages = [ 
    {
        "role": "system", 
        "content": json_parser.get_format_instructions()}, 
    { 
        "role": "user", 
        "content": "Generate 5 random prime numbers between 1,000 and 100,000, and indicate the number of prime numbers less than each of them.", 
    }, 
] 

resp = llm.invoke(messages) 
json_resp = json_parser.invoke(resp)
print(json_resp) 

# {'prime': [14593, 22817, 51787, 68437, 91703], 'count': [1710, 2545, 5301, 6799, 8862]}