import json
import os
import requests
from dotenv import load_dotenv
from gradio_client import Client

load_dotenv()

class GradioClientModerator:
    def __init__(self, model_name="duchaba/Friendly_Text_Moderation"):
        self.client = Client(model_name)

    def moderate(self, text: str, safer: float = 0.02) -> dict:
        try:
            result = self.client.predict(
                msg=text,
                safer=safer,
                api_name="/fetch_toxicity_level"
            )
            json_data = json.loads(result[1])
            return json_data
        except Exception as e:
            return {"error": str(e)}


class HuggingFaceAPIModerator:
    def __init__(self):
        self.api_url = "https://api-inference.huggingface.co/models/ML6team/friendly-text-moderator"
        self.headers = {
            "Authorization": f"Bearer {os.getenv('HF_API_KEY')}",
            "Content-Type": "application/json"
        }

    def moderate(self, text: str) -> dict:
        try:
            response = requests.post(
                self.api_url,
                headers=self.headers,
                json={"inputs": text}
            )
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            return {"error": str(e)}
