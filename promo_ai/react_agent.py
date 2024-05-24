from typing import List

import streamlit as st
from promo_ai.promo_json import make_promo_understander
from promo_ai.prompts import react_prompt

from llama_index.core.tools import FunctionTool, BaseTool
from llama_index.core.agent import ReActAgent
from llama_index.core.llms import ChatMessage
from llama_index.llms.ollama import Ollama


@st.cache_resource()    
def make_react_agent() -> ReActAgent:
    """
    Agent that drives the flow. Has an array of tools it selects from to commit actions.
    """
    
    json_creator_func = make_promo_understander().send_message
    promo_json_tool = FunctionTool.from_defaults(
        fn=json_creator_func,
        name="promo_code_json",
        description="A tool that creates promo code JSON from a description of a promo code.",
        fn_schema=ChatMessage
    )

    def create_code(**kwargs) -> str:
        print(st.session_state["promo_json"])
        return "it did the thing"

    tools: List[BaseTool] = [
        promo_json_tool,
        FunctionTool.from_defaults(
            fn=create_code,
            name="promo_code_api_create",
            description="A tool that creates a promo code",
        )
    ]

    llm = Ollama(model="llama3", request_timeout=120, temperature=0)
    react_agent = ReActAgent.from_tools(tools=tools, llm=llm, verbose=True, context=react_prompt)

    return react_agent