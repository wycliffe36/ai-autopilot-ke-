import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="AI Autopilot KE", page_icon="🤖")

st.title("🤖 AI Autopilot KE")
st.write("Your free AI assistant for Kenya")

# Get key from secrets
GEMINI_KEY = os.getenv("GEMINI_KEY")

# CHECK IF KEY EXISTS
if not GEMINI_KEY:
    st.error("🚨 KEY NOT FOUND! \n\n Go to Manage app → Settings → Secrets \n\n Add this: \n GEMINI_KEY=\"your-key-here\"")
    st.stop()

# Configure Gemini
try:
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')
except Exception as e:
    st.error(f"🚨 KEY ERROR: {e}")
    st.stop()


# Chat input
prompt = st.chat_input("Ask me anything...")

if prompt:
    with st.spinner("Thinking..."):
        try:
            response = model.generate_content(prompt)
            st.write(response.text)
        except Exception as e:
            st.error(f"🚨 API ERROR: {e}")
            st.info("This usually means: Wrong key, or you need to wait 1 min after reboot")
