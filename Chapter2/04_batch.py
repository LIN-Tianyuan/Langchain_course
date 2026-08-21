#  pip install langchain-openai

# Retrieve API Key → Create a Large Model → Prepare Conversation Messages → Call the Model → Get the AI Response

import os 
from langchain.chat_models import init_chat_model 
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv 

load_dotenv() # Load .env by default

llm = init_chat_model( 
    model="gpt-5.4", 
    model_provider="openai", 
) 

messages = [ 
    [ 
        {"role": "system", "content": "你是一位诗人"}, 
        {"role": "user", "content": "写一首关于春天的诗"}, 
    ], 
    [ 
        {"role": "system", "content": "你是一位诗人"}, 
        {"role": "user", "content": "写一首关于夏天的诗"}, 
    ], 
    [ 
        {"role": "system", "content": "你是一位诗人"}, 
        {"role": "user", "content": "写一首关于秋天的诗"}, 
    ], 
] 
resp = llm.batch(messages) # Batch call; returns a list of messages
print(resp)