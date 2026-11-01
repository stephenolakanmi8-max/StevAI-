import streamlit as st
import time
import random

st.set_page_config(page_title="StevAI", page_icon="🚀", layout="centered")
st.title("StevAI - Your AI Assistant 🚀")

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hey Stephen! I'm StevAI! Ask me anything 😎"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

if prompt := st.chat_input("Ask StevAI anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            time.sleep(1)
        replies = [f"You asked: '{prompt}' - StevAI is learning!", f"Interesting question about '{prompt}'! 🔥", f"Hey! For '{prompt}', let's build the future together!"]
        response = random.choice(replies)
        st.write(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
