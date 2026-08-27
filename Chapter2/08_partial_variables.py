from langchain_core.prompts import PromptTemplate 

template = PromptTemplate( 
    template="{foo} {bar}", 
    input_variables=["foo", "bar"], 
    partial_variables={"foo": "hello"}, # Predefine Some Variables
) 

prompt = template.format(bar="world") 

print(prompt) # hello world