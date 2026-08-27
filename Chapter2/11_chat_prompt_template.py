from langchain_core.prompts import ChatPromptTemplate 

template = ChatPromptTemplate( 
    [ 
        ("system", "You are an AI development engineer, and your name is {name}。"), 
        ("human", "What can you do for me?"), 
        ("ai", "I can develop a lot of {thing}。"), 
        ("human", "{user_input}"), 
    ] 
) 

prompt = template.format_messages(name="Lemon AI", thing="AI", user_input="行") 
print(prompt) 
# [
#   SystemMessage(content='You are an AI development engineer, and your name is Lemon AI。', ..., 
#   HumanMessage(content='What can you do for me?', ...), 
#   AIMessage(content='I can develop a lot of AI。', ...),
#   HumanMessage(content='行', ...)
# ]