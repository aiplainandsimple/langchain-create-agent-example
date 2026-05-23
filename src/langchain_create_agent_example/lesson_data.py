"""Small deterministic data layer used by the agent tool and tests."""

from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True)
class LearningPath:
    """A compact lesson recommendation for a LangChain concept."""

    topic: str
    first_step: str
    why_it_matters: str
    next_step: str


LEARNING_PATHS: dict[str, LearningPath] = {
    "agents": LearningPath(
        topic="agents",
        first_step="Create one agent with one simple tool.",
        why_it_matters="Agents become easier to understand when you can see the model decide whether to call a tool.",
        next_step="Add a second tool and compare which tool the model chooses for different questions.",
    ),
    "tools": LearningPath(
        topic="tools",
        first_step="Write a regular Python function with a clear docstring, then decorate it with @tool.",
        why_it_matters="The function name, arguments, and docstring help the model understand when to use the tool.",
        next_step="Try changing the docstring and observe how the agent's behavior changes.",
    ),
    "messages": LearningPath(
        topic="messages",
        first_step="Pass a list of role/content messages into agent.invoke.",
        why_it_matters="Messages are the conversation state the agent reads before it decides what to do.",
        next_step="Send a follow-up message and include the earlier assistant response in the message list.",
    ),
}

DEFAULT_TOPIC = "agents"


def normalize_topic(topic: str) -> str:
    """Normalize user input into a known learning-path topic."""

    clean_topic = topic.strip().lower()
    if clean_topic in LEARNING_PATHS:
        return clean_topic
    return DEFAULT_TOPIC


def build_learning_recommendation(topic: str) -> str:
    """Return a short recommendation for a LangChain learning topic."""

    path = LEARNING_PATHS[normalize_topic(topic)]
    return (
        f"Topic: {path.topic}\n"
        f"First step: {path.first_step}\n"
        f"Why it matters: {path.why_it_matters}\n"
        f"Next step: {path.next_step}"
    )
