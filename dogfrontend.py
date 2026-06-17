import streamlit as st
from dog import action

st.title("chat with chive")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    avatar = "chive.jpeg" if msg["role"] == "assistant" else None
    with st.chat_message(msg["role"], avatar=avatar):
        st.write(msg["content"])

ui = st.chat_input("Say something to Chive!")
if ui:
    st.session_state.messages.append({"role": "user", "content": ui})
    reply = action(ui)
    st.session_state.messages.append({"role": "assistant", "content": reply})
    st.rerun()
