# Friendly Text Moderator

A simple Streamlit app that uses the HuggingFace Friendly Text Moderator API from https://huggingface.co/spaces/duchaba/Friendly_Text_Moderation
to moderate text. The app allows users to input text and get a moderation score, as well as a list of offensive words.

## Prerequisites

- **Python 3.8+**
- **HuggingFace API Key**: You need to create a HuggingFace account and get an API key. You can sign up for free at [HuggingFace](https://huggingface.co/join). Once you have an account, you can find your API key in your account settings.

## Setup

1. Clone the repo
   ```bash
   git clone https://github.com/devendersharma-mset/friendly-text-moderator-app.git
    ```
2. Create a `.env` file with your HuggingFace API token. i.e. add:
   ```bash
   HF_API_KEY=<token>
   ```
3. Install dependencies:
   ```bash
   python -m venv venv             
   source venv/bin/activate  # On Windows run: venv\Scripts\activate
   pip install -r requirements.txt
    ```
4. Run app and test the model
   ```bash
    streamlit run app.py
    ```
5. Open your browser and go to `http://localhost:8501` to see the app in action.
