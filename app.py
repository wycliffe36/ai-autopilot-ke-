
import streamlit as st
from google import genai
import os

st.set_page_config(page_title="AI Autopilot KE", page_icon="🚀")
st.title("🚀 AI Autopilot KE")
st.caption("Powered by Gemini 2.0 Flash")

client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

if prompt := st.chat_input("Ask me anything..."):
    with st.spinner("Thinking..."):
        res = client.models.generate_content(
            model="gemini-2.0-flash", 
            contents=prompt
        )
    st.write(res.text)
