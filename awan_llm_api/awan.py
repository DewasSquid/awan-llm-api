from typing import Any
import requests
import json
from awan_llm_api.completions import Completions, ChatCompletions
from awan_llm_api.utils.enums import AwanLLMEndpoints


class AwanLLMClient:
    def __init__(self, api_key: str):
        """
        Initializes an AwanLLMClient instance.

        Args:
            api_key (str): The API key for authenticating with the AwanLLM API.
        """
        self.api_key = api_key
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': f"Bearer {self.api_key}"
        }

    def _post_request(self, url: str, payload: dict):
        response = requests.post(url, headers=self.headers, data=json.dumps(payload))
        response.raise_for_status()
        return response.json()

    def completion(self, completions: Completions, options: dict[str, Any] = {}):
        """
        Sends a completion request to the AwanLLM API.

        Args:
            completions (Completions): The completions object containing the request details.
            options (dict, optional): Additional options for the completion request. Defaults to {}.

        Returns:
            dict: The response from the API.
        """
        payload = completions._get_payload(options)
        return self._post_request(AwanLLMEndpoints.COMPLETIONS.value, payload)

    def chat_completion(self, chat_completions: ChatCompletions, options: dict[str, Any] = {}):
        """
        Sends a chat completion request to the AwanLLM API.

        Args:
            chat_completions (ChatCompletions): The chat completions object containing the request details.
            options (dict, optional): Additional options for the chat completion request. Defaults to {}.

        Returns:
            dict: The response from the API.
        """
        payload = chat_completions._get_payload(options)
        return self._post_request(AwanLLMEndpoints.CHAT_COMPLETIONS.value, payload)