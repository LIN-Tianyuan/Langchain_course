import os 
from langchain.chat_models import init_chat_model 
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv 

load_dotenv() # Load .env by default

llm = init_chat_model( 
    model="gpt-5.4", 
    model_provider="openai", 
) 


template = ChatPromptTemplate( 
    [ 
        {"role": "system", "content": "Briefly describe the content of the image in English."}, 
        {"role": "user", "content": [{"image_url": "{image_url}"}]}, 
    ] 
) 

prompt = template.format_messages( 
    image_url="https://upload.wikimedia.org/wikipedia/commons/3/3a/Cat03.jpg" 
) 

resp = llm.invoke(prompt) 
print(resp.content)