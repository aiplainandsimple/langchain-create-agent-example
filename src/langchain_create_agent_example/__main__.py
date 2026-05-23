"""Command line entrypoint for the LangChain create_agent example."""

from __future__ import annotations

import argparse

from langchain_create_agent_example.agent import ask_agent


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Ask a tiny LangChain create_agent learning assistant a question.",
    )
    parser.add_argument(
        "question",
        nargs="?",
        default="What should I learn first for LangChain agents?",
        help="Question to send to the agent.",
    )
    return parser


def main() -> None:
    args = build_parser().parse_args()
    print(ask_agent(args.question))


if __name__ == "__main__":
    main()
