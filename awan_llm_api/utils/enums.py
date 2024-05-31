from enum import Enum


class AwanLLMEndpoints(Enum):
    CHAT_COMPLETIONS = "https://api.awanllm.com/v1/chat/completions"
    COMPLETIONS = "https://api.awanllm.com/v1/completions"


class Role(Enum):
    USER = "user"
    ASSISTANT = "assistant"
    SYSTEM = "system"
