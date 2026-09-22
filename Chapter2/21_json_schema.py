from langchain.chat_models import init_chat_model
from dotenv import load_dotenv 

load_dotenv() # Load .env by default

llm = init_chat_model( 
    model="gpt-5.4", 
    model_provider="openai", 
)

schema = {
    "name": "animal_list",
    "schema": {
        "type": "object",
        "properties": {
            "animals": {
                "type": "array",
                "items": {
                    "type": "object",
                    "properties": {
                        "animal": {
                            "type": "string",
                            "description": "Animal Name"
                        },
                        "emoji": {
                            "type": "string",
                            "description": "Animal Emoji"
                        },
                    },
                    "required": ["animal", "emoji"],
                    "additionalProperties": False,
                },
            }
        },
        "required": ["animals"],
        "additionalProperties": False,
    },
}

messages = [{"role": "user", "content": "Randomly generate three animals and their corresponding emojis"}] 

llm_with_structured_output = llm.with_structured_output( 
    schema, method="json_schema", include_raw=True 
) 
resp = llm_with_structured_output.invoke(messages) 
print(resp) 
print(resp["raw"]) 
print(resp["parsed"]) 
"""
{'raw': AIMessage(content='{"animals":[{"animal":"Fox","emoji":"🦊"},{"animal":"Elephant","emoji":"🐘"},{"animal":"Penguin","emoji":"🐧"}]}', additional_kwargs={'parsed': None, 'refusal': None}, response_metadata={'token_usage': {'completion_tokens': 42, 'prompt_tokens': 73, 'total_tokens': 115, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}}, 'model_provider': 'openai', 'model_name': 'gpt-5.4-2026-03-05', 'system_fingerprint': None, 'id': 'chatcmpl-EQuVUHhqbi95w7zHiJyw79kOF3Y3Q', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None}, id='lc_run--01a0c93a-b6df-7431-b9cb-5a7a89d58f26-0', tool_calls=[], invalid_tool_calls=[], usage_metadata={'input_tokens': 73, 'output_tokens': 42, 'total_tokens': 115, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}), 'parsed': {'animals': [{'animal': 'Fox', 'emoji': '🦊'}, {'animal': 'Elephant', 'emoji': '🐘'}, {'animal': 'Penguin', 'emoji': '🐧'}]}, 'parsing_error': None}
content='{"animals":[{"animal":"Fox","emoji":"🦊"},{"animal":"Elephant","emoji":"🐘"},{"animal":"Penguin","emoji":"🐧"}]}' additional_kwargs={'parsed': None, 'refusal': None} response_metadata={'token_usage': {'completion_tokens': 42, 'prompt_tokens': 73, 'total_tokens': 115, 'completion_tokens_details': {'accepted_prediction_tokens': 0, 'audio_tokens': 0, 'reasoning_tokens': 0, 'rejected_prediction_tokens': 0, 'text_tokens': None}, 'prompt_tokens_details': {'audio_tokens': 0, 'cache_write_tokens': None, 'cached_tokens': 0, 'image_tokens': None, 'text_tokens': None}}, 'model_provider': 'openai', 'model_name': 'gpt-5.4-2026-03-05', 'system_fingerprint': None, 'id': 'chatcmpl-EQuVUHhqbi95w7zHiJyw79kOF3Y3Q', 'service_tier': 'default', 'finish_reason': 'stop', 'logprobs': None} id='lc_run--01a0c93a-b6df-7431-b9cb-5a7a89d58f26-0' tool_calls=[] invalid_tool_calls=[] usage_metadata={'input_tokens': 73, 'output_tokens': 42, 'total_tokens': 115, 'input_token_details': {'audio': 0, 'cache_read': 0}, 'output_token_details': {'audio': 0, 'reasoning': 0}}
{'animals': [{'animal': 'Fox', 'emoji': '🦊'}, {'animal': 'Elephant', 'emoji': '🐘'}, {'animal': 'Penguin', 'emoji': '🐧'}]}
"""