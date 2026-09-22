from pydantic import BaseModel, Field 
from langchain.chat_models import init_chat_model
from dotenv import load_dotenv 

load_dotenv() # Load .env by default

llm = init_chat_model( 
    model="gpt-5.4", 
    model_provider="openai", 
) 

class Animal(BaseModel): 
    animal: str = Field(description="Animal") 
    emoji: str = Field(description="Emoji") 

class AnimalList(BaseModel): 
    animals: list[Animal] = Field(description="List of animals with their emoji") 

messages = [
    {
        "role": "user", 
        "content": "Randomly generate three animals and their corresponding emojis"
    }
] 

llm_with_structured_output = llm.with_structured_output(AnimalList) 
resp = llm_with_structured_output.invoke(messages) 
print(resp)

# animals=[Animal(animal='Tiger', emoji='🐯'), Animal(animal='Penguin', emoji='🐧'), Animal(animal='Octopus', emoji='🐙')]