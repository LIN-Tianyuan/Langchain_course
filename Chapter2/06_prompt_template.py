from langchain_core.prompts import PromptTemplate 

# Instantiate a prompt template using a constructor 
template = PromptTemplate(
    template="Please evaluate the pros and cons of {product}, including {aspect1} and {aspect2}.",
    input_variables=["product", "aspect1", "aspect2"], 
) 

# Generate Prompts Using Templates
prompt_1 = template.format(product="smartphones", aspect1="battery life", aspect2="camera quality") 
prompt_2 = template.format(product="laptops", aspect1="processing speed", aspect2="portability") 

print(prompt_1) # Please evaluate the pros and cons of smartphones, including battery life and camera quality.
print(prompt_2) # Please evaluate the pros and cons of laptops, including processing speed and portability.