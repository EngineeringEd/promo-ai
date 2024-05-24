from typing import List

from llama_index.core.llms import ChatMessage, MessageRole, ChatResponse
from llama_index.llms.ollama import Ollama

from promo_ai.prompts import full_prompt, correcting_prompts
import streamlit as st


class PromoUnderstander:
    """
    Takes a message from another place and tries it's best to create promocode JSON
    """

    _msgs: List[ChatMessage]
    _llm: Ollama 

    def __init__(self) -> None:
        self._llm = Ollama(model="codellama", request_timeout=120, temperature=0)
        self._msgs = []

        first = ChatMessage(role=MessageRole.SYSTEM, content=full_prompt)

        self._msgs.append(first)

        for p in correcting_prompts:
            self._msgs.append(ChatMessage(role=MessageRole.SYSTEM, content=p))

    
    def send_message(self, **kwargs) -> ChatResponse:
        self._msgs.append(ChatMessage(content=str(kwargs["content"])))
        res = self._llm.chat(self._msgs)
        st.session_state["promo_json"] = res.message.content
        
        return self._llm.chat(self._msgs)
    

@st.cache_resource()
def make_promo_understander() -> PromoUnderstander:
    return PromoUnderstander()

    