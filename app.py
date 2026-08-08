    import streamlit as st

    from google import genai
    import os

    st.title("🚀 AI Autopilot KE")
    client = genai.Client(api_key=os.getenv("GEMINI_KEY"))

    if prompt := st.chat_input("Ask me anything"):
        res = client.models.generate_content(model="gemini-2.5-flash", contents=prompt)
        st.write(res.text)


