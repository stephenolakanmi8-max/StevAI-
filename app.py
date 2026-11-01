import streamlit as st
from openai import OpenAI

st.set_page_config(page_title="StevAI", page_icon="🤖")
st.title("🤖 StevAI")
st.caption("Powered by Gemini 4 Argon - Built by Stephen")

api_key = st.secrets.get("OPENROUTER_API_KEY", "")

if not api_key:
    st.warning("Add OPENROUTER_API_KEY in Streamlit Secrets!")
    st.stop()

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=api_key,
)

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "Hello! I'm StevAI powered by Gemini 4 Argon! How can I help you? 🚀"}]

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

if prompt := st.chat_input("Ask StevAI anything..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)
    with st.chat_message("assistant"):
        response = client.chat.completions.create(
          model="google/gemini-4-argon",
          messages=st.session_state.messages
        )
        answer = response.choices[0].message.content
        st.markdown(answer)
        st.session_state.messages.append({"role": "assistant", "content": answer})
