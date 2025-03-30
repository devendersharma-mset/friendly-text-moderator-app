import streamlit as st
from moderator import TextModerator

st.set_page_config(page_title="Friendly Text Moderator", layout="centered")

st.title("🤖 Friendly Text Moderator")
st.write("Check if your text is safe, friendly, and appropriate.")

# Initialize the moderator with default mode = gradio_client
moderator = TextModerator(mode="gradio_client")

# Text input
user_input = st.text_area("Enter your text below:")

# Threshold slider
safer_threshold = st.slider(
    "Choose Safer Threshold (lower = more strict)",
    min_value=0.0,
    max_value=1.0,
    value=0.02,
    step=0.01
)

# Button
if st.button("Moderate Text"):
    if user_input.strip():
        with st.spinner("Moderating..."):
            try:
                result = moderator.moderate(user_input, safer_threshold)
                st.success("Moderation Complete!")
                st.json(result)
            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text to moderate.")
