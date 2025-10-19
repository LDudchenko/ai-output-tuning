from task.app.clients.anthropic_client import AnthropicAIClient
from task.app.clients.openai_client import OpenAIClient
from task.app.main import run

# TODO:
#  Try `stop`(for OpenAI) and `stop_sequences` (for Anthropic) parameters.
#  `stop` (str or list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  `stop_sequences` (list[str]): Tells the AI to stop generating text when it encounters specific words or phrases.
#  Like setting custom "end of response" triggers.
#       Default: None
#  User massage: Explain the key components of a Large Language Model architecture

run(
    OpenAIClient("gpt-4o"),
    print_request=True,
    print_only_content=False,
    stop="\n\n"
)


run(
    OpenAIClient("gpt-4o"),
    print_request=True,
    print_only_content=False,
    stop=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
)

run(
    AnthropicAIClient("claude-3-haiku-20240307"),
    print_request=True,
    print_only_content=False,
    stop_sequences=["**Embedding Layer**", "**Transformer Blocks**", "**Training**"]
)



# With `stop` parameter we can stop content generation. It can be used for some policies/guardrails. For instance,
# we are the company with the name `Pear` and we don't want that anybody will see in results that our competitor `Apple`
# is cool (stop: ["Apple is cool", "Apple top"]).