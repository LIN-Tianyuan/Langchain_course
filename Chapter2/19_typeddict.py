from typing import TypedDict, Annotated 
from langchain.chat_models import init_chat_model 

from dotenv import load_dotenv 

load_dotenv() # Load .env by default

llm = init_chat_model( 
    model="gpt-5.4", 
    model_provider="openai", 
) 

class Animal(TypedDict): 
    animal: Annotated[str, "Animal"] 
    emoji: Annotated[str, "Emoji"] 

class AnimalList(TypedDict): 
    animals: Annotated[list[Animal], "List of animals with their emoji"] 
    
messages = [{"role": "user", "content": "Randomly generate three animals and their corresponding emojis"}] 

llm_with_structured_output = llm.with_structured_output(AnimalList) 
resp = llm_with_structured_output.invoke(messages) 
print(resp) 
# {'animals': [{'animal': 'Tiger', 'emoji': '🐯'}, {'animal': 'Penguin', 'emoji': '🐧'}, {'animal': 'Octopus', 'emoji': '🐙'}]}