import streamlit as st

# Page Config
st.set_page_config(page_title="AI Autopilot KE", page_icon="🚀", layout="centered")

# Title + Hackathon Badge
st.title("🚀 AI Autopilot KE")
st.markdown("**🚀 Submitted for GenAI Exchange Hackathon 2026 | Nairobi, Kenya**")
st.write("")

# New Tagline
st.write("AI Autopilot KE: Get personalized career guidance, CV help, and interview prep in Swahili, Sheng, and English. Built for Kenyan youth by Kenyan youth.")
st.write("---")

# Input Section
st.subheader("Tell me about yourself")
user_goal = st.text_area("What career help do you need today?", 
                         placeholder="e.g. Help me write a CV, Prepare for interview, Choose a career path")

language = st.selectbox("Pick your language", ["English", "Swahili", "Sheng"])

if st.button("Get AI Guidance"):
    if user_goal:
        with st.spinner("Your AI Career Coach is thinking..."):
            # This is where your AI logic will go
            st.success(f"Asante! Here is AI guidance in {language} for: {user_goal}")
            st.info("This is a demo response. Connect your AI model here to give real advice.")
    else:
        st.warning("Please tell me what help you need first.")

st.write("---")
st.caption("Built with ❤️ for Kenyan Youth | GenAI Exchange Hackathon 2026")
