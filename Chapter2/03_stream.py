#  pip install langchain-openai

# Retrieve API Key → Create a Large Model → Prepare Conversation Messages → Call the Model → Get the AI Response

import os 
from langchain.chat_models import init_chat_model 
from langchain.messages import SystemMessage, HumanMessage, AIMessage
from dotenv import load_dotenv 

load_dotenv() # Load .env by default

# Create a chat model
# Here, LangChain serves as a unified interface. 
# For example, if we switch to another model provider in the future, the overall calling method can remain as consistent as possible.
llm = init_chat_model( 
    model="gpt-5.4", 
    model_provider="openai", 
) 

# messages = [
#     # Set Roles and Rules for AI
#     SystemMessage(content="你是一个诗人"),
#     # Questions actually asked by users
#     HumanMessage(content="写一首关于春天的诗"), 
# ] 

messages = [ 
    {"role": "system", "content": "你是个诗人"}, 
    {"role": "user", "content": "写首关于春天的诗"}, 
]

# Use the `stream()` method for streaming output
for chunk in llm.stream(messages): 
    # Print content blocks one by one and refresh the buffer to display the content immediately
    print(chunk.content, end="", flush=True) 