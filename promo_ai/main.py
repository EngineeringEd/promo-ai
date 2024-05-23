from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage, MessageRole
from promo_ai.prompts import full_prompt

def main():
    llm = Ollama(model="codellama", request_timeout=120)

    first = ChatMessage(role=MessageRole.SYSTEM, content=full_prompt)
    second = ChatMessage(role=MessageRole.USER, content="Create a promo code that gives me £5 off my first booking")

    messages = [
        first,
        second
    ]

    res = llm.chat(messages)

    print(res)