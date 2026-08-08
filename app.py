import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="AI Autopilot KE", page_icon="🤖")

st.title("AI Autopilot KE")
st.write("Welcome to your AI assistant")

GEMINI_KEY = st.secrets["GEMINI_KEY"]
genai.configure(api_key=GEMINI_KEY)

prompt = st.text_input("Ask me anything:")

if st.button("Send"):
    model = genai.GenerativeModel("gemini-1.0-pro")
    response = model.generate_content(prompt)
    st.write(response.text)
