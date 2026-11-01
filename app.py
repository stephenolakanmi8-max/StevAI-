   import streamlit as st
   st.title("StevAI is Live! 🚀")
   st.write("Welcome to my AI app by Stephen!")
   name = st.text_input("Your name?")
   if name:
       st.success(f"Hello {name}!")
