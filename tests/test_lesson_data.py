from langchain_create_agent_example.lesson_data import (
    DEFAULT_TOPIC,
    build_learning_recommendation,
    normalize_topic,
)


def test_normalize_topic_accepts_known_topic_with_whitespace() -> None:
    assert normalize_topic("  Tools ") == "tools"


def test_normalize_topic_falls_back_to_default() -> None:
    assert normalize_topic("retrieval") == DEFAULT_TOPIC


def test_build_learning_recommendation_contains_expected_sections() -> None:
    recommendation = build_learning_recommendation("messages")

    assert "Topic: messages" in recommendation
    assert "First step:" in recommendation
    assert "Why it matters:" in recommendation
    assert "Next step:" in recommendation
