"""A minimal LangChain create_agent example."""

from __future__ import annotations

import os

from dotenv import load_dotenv
from langchain.agents import create_agent
from langchain.tools import tool

from langchain_create_agent_example.lesson_data import build_learning_recommendation

DEFAULT_MODEL = "openai:gpt-4o-mini"

SYSTEM_PROMPT = """You are a friendly LangChain tutor.
When a learner asks what to study, use the recommendation tool.
Keep the final answer concise and practical.
"""


@tool
def recommend_learning_path(topic: str) -> str:
    """Recommend a first learning step for a LangChain topic.

    Args:
        topic: A topic such as agents, tools, or messages.
    """

    return build_learning_recommendation(topic)


def create_learning_agent(model: str | None = None):
    """Create the example LangChain agent."""

    load_dotenv()
    selected_model = model or os.getenv("LANGCHAIN_MODEL", DEFAULT_MODEL)
    return create_agent(
        model=selected_model,
        tools=[recommend_learning_path],
        system_prompt=SYSTEM_PROMPT,
    )


def ask_agent(question: str, model: str | None = None) -> str:
    """Ask the example agent one question and return its final message text."""

    agent = create_learning_agent(model=model)
    result = agent.invoke({"messages": [{"role": "user", "content": question}]})
    final_message = result["messages"][-1]
    content = final_message.content

    if isinstance(content, str):
        return content
    return str(content)
