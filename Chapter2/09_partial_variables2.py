from langchain_core.prompts import PromptTemplate 

template = PromptTemplate.from_template("{foo} {bar}") 
partial_template = template.partial(foo="hello") # Predefine some variables

prompt = partial_template.format(bar="world") 

print(prompt) # hello world 