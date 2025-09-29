import os
import json
import secrets
from pathlib import Path
from datetime import datetime

from pydantic_ai.messages import ModelMessagesTypeAdapter


LOG_DIR = Path(os.getenv("LOGS_DIRECTORY", "logs"))
LOG_DIR.mkdir(exist_ok=True)


def log_entry(agent, messages, source="user"):
    tools = []

    for ts in agent.toolsets:
        tools.extend(ts.tools.keys())

    dict_messages = ModelMessagesTypeAdapter.dump_python(messages)

    return {
        "agent_name": agent.name,
        "system_prompt": agent._instructions,
        "provider": agent.model.system,
        "model": agent.model.model_name,
        "tools": tools,
        "messages": dict_messages,
        "source": source,
    }


def serializer(obj):
    if isinstance(obj, datetime):
        return obj.isoformat()
    raise TypeError(f"Type {type(obj)} not serializable")


def log_interaction_to_file(
    agent=None,
    messages=None,
    source="user",
    agent_name=None,
    user_prompt=None,
    agent_response=None,
    timestamp=None,
):
    """
    Log an agent interaction to a JSON file.

    Can be called in two ways:
    1. With agent and messages (from main.py)
    2. With individual parameters (from app.py)
    """
    if agent is not None and messages is not None:
        # Called from main.py style
        entry = log_entry(agent, messages, source)
        agent_name_for_file = agent.name
    elif (
        agent_name is not None
        and user_prompt is not None
        and agent_response is not None
    ):
        # Called from app.py style
        # Create a minimal entry structure
        entry = {
            "agent_name": agent_name,
            "system_prompt": "GitSensei System Prompt",
            "provider": "Google",
            "model": "gemini-2.0-flash",
            "tools": ["search"],
            "messages": [
                {
                    "role": "user",
                    "content": user_prompt,
                    "timestamp": timestamp or datetime.now().isoformat(),
                },
                {
                    "role": "assistant",
                    "content": agent_response,
                    "timestamp": timestamp or datetime.now().isoformat(),
                },
            ],
            "source": source,
        }
        agent_name_for_file = agent_name
    else:
        raise ValueError(
            "Invalid parameters. Provide either (agent, messages) or (agent_name, user_prompt, agent_response)"
        )

    # Use timestamp from messages or current time
    if messages and entry["messages"]:
        ts = entry["messages"][-1].get("timestamp", datetime.now())
    else:
        ts = datetime.now()

    if isinstance(ts, str):
        # Parse ISO string back to datetime if needed
        try:
            ts = datetime.fromisoformat(ts.replace("Z", "+00:00"))
        except Exception:
            ts = datetime.now()

    ts_str = ts.strftime("%Y%m%d_%H%M%S")
    rand_hex = secrets.token_hex(3)

    filename = f"{agent_name_for_file}_{ts_str}_{rand_hex}.json"
    filepath = LOG_DIR / filename

    with filepath.open("w", encoding="utf-8") as f_out:
        json.dump(entry, f_out, indent=2, default=serializer)

    return filepath
