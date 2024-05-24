import streamlit as st
from llama_index.core.agent import AgentChatResponse

from promo_ai.react_agent import make_react_agent


agent = make_react_agent()
st.title("Chat with Promocodes")
st.caption("Powered by llamas")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "Assistant", "content": "hello"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "User", "content": prompt})
    st.chat_message("User").write(prompt)

    with st.spinner():
        res: AgentChatResponse = agent.chat(prompt)

    st.chat_message("Assistant").write(st.session_state["promo_json"])
    st.chat_message("Assistant").write(res.response)
    st.session_state.messages.append({"role": "Assistant", "content": res.response})

    