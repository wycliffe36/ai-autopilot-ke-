
import streamlit as st
from google import genai
import os

st.set_page_config(page_title="AI Autopilot KE", page_icon="🤖")

st.title("🤖 AI Autopilot KE")
st.write("Your free AI assistant for Kenya")

# Get key from secrets
try:
    API_KEY = st.secrets["GEMINI_KEY"]
except:
    st.error("KEY NOT FOUND! Add GEMINI_KEY to Streamlit Secrets")
    st.stop()

# New Gemini Client
client = genai.Client(api_key=API_KEY)

user_input = st.chat_input("Ask me anything...")

if user_input:
    with st.spinner("Thinking..."):
        try:
            response = client.models.generate_content(
                model='gemini-2.0-flash', 
                contents=user_input
            )
            st.write(response.text)
        except Exception as e:
            st.error(f"API ERROR: {e}")
            st.info("This usually means: Wrong key, or you need to wait 1 min after reboot")
