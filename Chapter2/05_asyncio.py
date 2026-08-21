import os 
import time 
import asyncio 
from langchain.chat_models import init_chat_model 
from dotenv import load_dotenv 

load_dotenv() # Load .env by default

llm = init_chat_model( 
    model="gpt-5.4", 
    model_provider="openai", 
) 


messagess = [ 
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

async def async_invoke(): 
    tasks = [llm.ainvoke(messages) for messages in messagess] 
    return await asyncio.gather(*tasks) 

start_time = time.time() 
resps = asyncio.run(async_invoke()) 
print(resps) 

end_time = time.time() 
print(f"Total time: {end_time - start_time}") 
# Total time: 5.208514928817749