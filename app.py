import streamlit as st
from moderator import TextModerator

st.set_page_config(page_title="Friendly Text Moderator", layout="centered")

st.title("🤖 Friendly Text Moderator")
st.write("Check if your text is safe, friendly, and appropriate.")

# Initialize the moderator
moderator = TextModerator()  # No mode param needed now

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
                result = moderator.moderate(user_input)

                # Extract dictionary from result
                if isinstance(result, list):
                    scores = result[0]  # First item is the dict
                else:
                    scores = result

                # Filter flagged categories
                flagged = {
                    k: v for k, v in scores.items()
                    if isinstance(v, float) and v > safer_threshold
                }

                st.success("Moderation Complete!")

                st.subheader("All Category Scores:")
                st.json(scores)

                if flagged:
                    st.error("⚠️ Flagged Categories:")
                    st.json(flagged)
                else:
                    st.info("✅ Text is within safe limits.")

            except Exception as e:
                st.error(f"Error: {str(e)}")
    else:
        st.warning("Please enter some text to moderate.")
