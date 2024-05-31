from typing import Any
from awan_llm_api.utils.enums import Role


class Completions:
    def __init__(self, model_name: str, prompt: str):
        self.model_name = model_name
        self.prompt = prompt

    def _get_payload(self, options: dict[str, Any]):
        return {
            "model": self.model_name,
            "prompt": self.prompt,
            **options
        }


class ChatCompletions:
    def __init__(self, model_name: str):
        self.model_name = model_name
        self.messages = []

    def add_message(self, role: Role, content: str):
        self.messages.append({"role": role.value, "content": content})

    def _get_payload(self, options: dict[str, Any]):
        return {
            "model": self.model_name,
            "messages": self.messages,
            **options
        }
