from langchain_core.prompts import ChatPromptTemplate 

template = ChatPromptTemplate.from_messages( 
    [ 
        ("system", "You are an assistant."), 
        ("placeholder", "{conversation}"), 
        # equivalent to MessagesPlaceholder(variable_name="conversation", optional=True) 
    ] 
) 

prompt = template.format_messages( 
    conversation=[ 
        ("human", "Hello! "), 
        ("ai", "Is there anything you'd like me to do for you? "), 
        ("human", "Could you make me some ice cream? "), 
        ("ai", "I couldn't do that. "), 
    ] 
) 

print(prompt) 
