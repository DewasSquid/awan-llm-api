# AwanLLM API Wrapper

This Python API wrapper provides an easy way to interact with the AwanLLM language models, allowing you to use the capabilities of the AwanLLM platform for generating text completions and chat-based interactions.

## Installation

To use this API wrapper, you need to have Python installed on your system. You can install the required library by running:

```bash
pip install awan-llm-api
```

## Usage

### Setting Up

First, you need to set up your API key and select a model. You can find the list of available models on the AwanLLM website.

```python
from awan_llm_api import AwanLLMClient, Role
from awan_llm_api.completions import Completions, ChatCompletions

AWANLLM_API_KEY = "YOUR_API_KEY"
MODEL = "Meta-Llama-3-8B-Instruct"  # Replace with your chosen model

client = AwanLLMClient(AWANLLM_API_KEY)
```

### Chat Completion Example

To generate a chat completion, you need to create a `ChatCompletions` instance, add messages to it, and then request a completion from the client.

```python
# Initialize a ChatCompletions instance
chat = ChatCompletions(MODEL)

# Add a user message to the chat
chat.add_message(Role.USER, "Hello !")

# Request a chat completion
chat_response = client.chat_completion(chat)

# Print the chat response
print(chat_response)
```

### Text Completion Example

To generate a text completion, you need to create a `Completions` instance with a prompt and then request a completion from the client.

```python
# Initialize a Completions instance with a prompt
completion = Completions(MODEL, "Here's how you can make a cake using pizza:")

# Request a text completion
completion_response = client.completion(completion)

# Print the completion response
print(completion_response)
```

## Getting Help

For more details, check the [AwanLLM API documentation](https://www.awanllm.com/docs).

## License

This project is licensed under the MIT License. See the LICENSE file for more details.