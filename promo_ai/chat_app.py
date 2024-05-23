import streamlit as st

from llama_index.core.llms import ChatMessage, MessageRole


st.title("Chat with Promocodes")
st.caption("Powered by llamas")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "assistant", "content": "hello"}]

for msg in st.session_state["messages"]:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)