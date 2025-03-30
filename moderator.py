import os
import json
import requests
from gradio_client import Client


class TextModerator:
    def __init__(self):
        self.client = Client("duchaba/Friendly_Text_Moderation")

    def moderate(self, text: str, safer_threshold: float = 0.02) -> dict:
        return self._moderate_via_gradio(text, safer_threshold)

    def _moderate_via_gradio(self, text: str, safer: float = 0.02) -> dict:
        result = self.client.predict(
            text,
            safer,
            api_name="/fetch_toxicity_level"
        )
        # Extract JSON string from result and convert to dict
        json_str = result[1]
        return json.loads(json_str)
