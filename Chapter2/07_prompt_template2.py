from langchain_core.prompts import PromptTemplate 

# Use the `from_template` method to instantiate a prompt template
# template = PromptTemplate.from_template("请给我一个关于{topic}的{type}解释。") 
template = PromptTemplate.from_template("Please give me a {type} explanation of {topic}.") 

# Generate Prompts Using Templates
prompt = template.format(type="detailed", topic="quantum mechanics") 

print(prompt) # Please give me a detailed explanation of quantum mechanics.