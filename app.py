import streamlit as st
from openai import OpenAI

# Page setup
st.set_page_config(page_title="StevAI", page_icon="🚀")
st.title("StevAI")
st.caption("Powered by Gemini - Built by Stephen 🚀")

# Get API key from Streamlit Secrets
try:
    api_key = st.secrets["OPENROUTER_API_KEY"]
except:
    st.error("❌ API Key not found! Go to Streamlit > Settings > Secrets and add OPENROUTER_API_KEY")
    st.stop()

# Create client for OpenRouter
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
)

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Hello! I'm StevAI powered by Gemini! How can I help you? 🚀"}
    ]

# Show old messages
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.write(msg["content"])

# User input
if prompt := st.chat_input("Ask StevAI anything..."):
    # Add user message
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = client.chat.completions.create(
                    model="google/gemini-2.0-flash-exp:free",
                    messages=st.session_state.messages
                )
                answer = response.choices[0].message.content
                st.write(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {e}")
                st.info("Check: 1) Your OpenRouter key is valid 2) You have credits at openrouter.ai/credits")
