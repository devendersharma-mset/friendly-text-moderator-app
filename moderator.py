import os
import json
import requests
from dotenv import load_dotenv

# Importing gradio_client if available
try:
    from gradio_client import Client
except ImportError:
    Client = None  # Optional fallback if gradio_client isn't installed

# Load environment variables from .env file
load_dotenv()


class TextModerator:
    def __init__(self, mode="gradio_client"):
        self.mode = mode

        if self.mode == "huggingface_direct":
            self.api_url = "https://api-inference.huggingface.co/models/ML6team/friendly-text-moderator"
            self.headers = {
                "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
                "Content-Type": "application/json"
            }

        elif self.mode == "gradio_client":
            if not Client:
                raise ImportError("Please install gradio_client: pip install gradio_client")
            self.client = Client("duchaba/Friendly_Text_Moderation")
        else:
            raise ValueError("Unsupported mode: choose 'huggingface_direct' or 'gradio_client'.")

    def moderate(self, text: str, safer_threshold: float = 0.02) -> dict:
        if self.mode == "huggingface_direct":
            return self._moderate_via_hf(text)
        elif self.mode == "gradio_client":
            return self._moderate_via_gradio(text, safer_threshold)

    def _moderate_via_hf(self, text: str) -> dict:
        response = requests.post(
            self.api_url,
            headers=self.headers,
            json={"inputs": text}
        )
        response.raise_for_status()
        return response.json()

    def _moderate_via_gradio(self, text: str, safer: float = 0.02) -> dict:
        result = self.client.predict(
            text,   # First positional argument: input message
            safer,  # Second positional argument: safer threshold
            api_name="/fetch_toxicity_level"
        )
        # Extract JSON string from result and convert to dict
        json_str = result[1]
        return json.loads(json_str)
