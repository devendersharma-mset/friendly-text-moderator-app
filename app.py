import streamlit as st
from moderator import GradioClientModerator, HuggingFaceAPIModerator

# Select backend
USE_GRADIO = True

if USE_GRADIO:
    moderator = GradioClientModerator()
else:
    moderator = HuggingFaceAPIModerator()

st.set_page_config(page_title="Friendly Text Moderator", layout="centered")

st.title("🤖 Friendly Text Moderator")
st.markdown("Check if your text is safe, friendly, and appropriate.")

user_input = st.text_area("Enter your text:")

if st.button("Moderate Text"):
    if user_input.strip():
        with st.spinner("Analyzing text..."):
            result = moderator.moderate(user_input)
        st.success("Moderation complete.")
        st.json(result)
    else:
        st.warning("⚠️ Please enter some text to moderate.")
