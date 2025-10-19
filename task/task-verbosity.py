from task.app.clients.openai_client import OpenAIClient
from task.app.main import run

run(
    OpenAIClient("gpt-5"),
    print_request=False,
    print_only_content=True,
    verbosity="high"
)
