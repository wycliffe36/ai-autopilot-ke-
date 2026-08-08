
import streamlit as st
import google.generativeai as genai
import os

st.set_page_config(page_title="AI Autopilot KE", page_icon="🚀", layout="centered")

st.title("🚀 AI Autopilot KE")
st.caption("Your 24/7 AI Assistant powered by Gemini")

# Get key from secrets
GEMINI_KEY = os.getenv("GEMINI_KEY")

if not GEMINI_KEY:
    st.error("GEMINI_KEY not found. Add it in Settings → Secrets")
    st.stop()

# Configure with REST so free keys work
genai.configure(api_key=GEMINI_KEY, transport="rest")

# Use the model that works with free keys
model = genai.GenerativeModel("gemini-1.5-flash-latest")

# Chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Show chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User input
if prompt := st.chat_input("Ask me anything..."):
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get AI response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            try:
                response = model.generate_content(prompt)
                answer = response.text
                st.markdown(answer)
                st.session_state.messages.append({"role": "assistant", "content": answer})
            except Exception as e:
                st.error(f"Error: {e}")

st.sidebar.success("✅ AI Autopilot KE is Online")
