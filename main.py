from awan_llm_api import AwanLLMClient, Role
from awan_llm_api.completions import Completions, ChatCompletions


AWANLLM_API_KEY = "API-KEY"
MODEL = "Meta-Llama-3-8B-Instruct"  # List can be found on the AwanLLM website

client = AwanLLMClient(AWANLLM_API_KEY)

# Example for chat completion
chat = ChatCompletions(MODEL)
chat.add_message(Role.USER, "Hello !")
chat_response = client.chat_completion(chat)
print(chat_response)

# Example for completion
completion = Completions(MODEL, "Here's how you can make a cake using pizza:")
completion_response = client.completion(completion)
print(completion_response)