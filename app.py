import streamlit as st

st.set_page_config(page_title="StevAI", page_icon="🚀", layout="centered")

st.title("StevAI is Live! 🚀")
st.write("Welcome! My AI app is live!")

name = st.text_input("Your name:")
if name:
    st.success(f"Hello {name}!")
    st.balloons()
