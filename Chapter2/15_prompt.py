from langchain_core.prompts import load_prompt 

template = load_prompt("prompts/prompt.json", encoding="utf-8") 
print(template.format(name="alex", adjective="funny")) 

