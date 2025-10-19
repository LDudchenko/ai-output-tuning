from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.clients.openai_client import OpenAIClient
from task.app.main import run

# TODO:
#  Try different models with such user request:
#  User massage: What LLMs can do?
#  ---
#  Anthropic models: https://docs.anthropic.com/en/docs/about-claude/models/overview
#  OpenAI models: https://platform.openai.com/docs/models
#  - 'gpt-4o'
#  - 'claude-3-haiku-20240307'


run(
    AnthropicAIClient("claude-3-haiku-20240307"),
    print_request=True,
    print_only_content=True,
)

run(
    OpenAIClient("gpt-4o"),
    print_request=True,
    print_only_content=True,
)