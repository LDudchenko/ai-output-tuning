from task.app.clients.openai_client import OpenAIClient
from task.app.main import run

run(
    OpenAIClient("gpt-5"),
    print_request=False,
    print_only_content=True,
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "weather_info",
            "schema": {
                "type": "object",
                "properties": {
                    "location": {"type": "string"},
                    "temperature_celsius": {"type": "number"}
                },
                "required": ["location", "temperature_celsius"]
            }
        }
    }
)
