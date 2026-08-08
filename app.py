    import streamlit as st
    import google.generativeai as genai
    import os

    # CONFIG
    st.set_page_config(page_title="AI Autopilot KE", page_icon="🤖", layout="centered")

    # GET API KEY FROM SECRETS
    GEMINI_KEY = st.secrets["GEMINI_KEY"]
    genai.configure(api_key=GEMINI_KEY)
    model = genai.GenerativeModel('gemini-1.5-flash')

    # HEADER
    st.title("🤖 AI Autopilot KE")
    st.subheader("24/7 Paid AI Chatbot")
    st.write("Powered by Gemini. M-Pesa integration coming next.")

    # CHAT
    if "messages" not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    if prompt := st.chat_input("Ask me anything..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = model.generate_content(prompt)
                st.markdown(response.text)
        
        st.session_state.messages.append({"role": "assistant", "content": response.text})
