import streamlit as st

st.title("StevAI is Live! 🚀")
st.write("Welcome! My AI app is live!")

name = st.text_input("Your name:")

if name:
    st.success(f"Hello {name}!")
    st.balloons()
