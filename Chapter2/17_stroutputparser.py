from langchain.chat_models import init_chat_model 
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv 

load_dotenv() # Load .env by default

llm = init_chat_model( 
    model="gpt-5.4", 
    model_provider="openai", 
) 

messages = [ 
    {"role": "system", "content": "You are a robot."}, 
    {"role": "user", "content": "Hello"}, 
] 

resp = llm.invoke(messages) 
print(resp) # content=‘Hello! How can I help you?’ additional_kwargs=......

str_resp = StrOutputParser().invoke(resp) 
print(str_resp) # Hello! How can I help you? 