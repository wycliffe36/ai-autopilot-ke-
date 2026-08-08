
import streamlit as st
from groq import Groq

st.set_page_config(page_title="AI Autopilot KE", page_icon="🤖")
st.title("🤖 AI Autopilot KE")
st.write("Your free AI assistant for Kenya")

try:
    API_KEY = st.secrets["GROQ_KEY"]
    client = Groq(api_key=API_KEY)
except:
    st.error("KEY NOT FOUND! Add GROQ_KEY to Streamlit Secrets")
    st.stop()

user_input = st.chat_input("Ask me anything...")

if user_input:
    with st.spinner("Thinking..."):
        response = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": user_input}]
        )
        st.write(response.choices[0].message.content)
