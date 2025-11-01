# Project Overview

This project is a Python-based ReAct agent built using the LangGraph framework. The agent is designed to interact with a DuckDB database, allowing users to query the database using natural language. The agent uses a large language model to understand the user's query, generate a SQL query, execute it against the database, and return the result.

The core logic is implemented in `src/react_agent/graph.py`, which defines the agent's state machine using LangGraph. The agent has access to a set of tools defined in `src/react_agent/tools.py` for interacting with the DuckDB database, including listing tables, getting table schemas, and executing queries. The agent's behavior is guided by a system prompt defined in `src/react_agent/prompts.py`.

# Building and Running

## Dependencies

The project's dependencies are listed in the `pyproject.toml` file. The main dependencies are:

*   langgraph
*   langchain-openai
*   langchain-anthropic
*   langchain
*   langchain-fireworks
*   python-dotenv
*   langchain-tavily
*   duckdb

## Running the project

The `README.md` file provides instructions on how to run the project. It involves setting up a `.env` file with API keys and then using the `langgraph` command-line tool to run the agent.

**Key commands:**

*   `langgraph dev --no-browser`: Run the agent in development mode.

## Testing

The project includes integration and unit tests in the `tests` directory.

*   `tests/integration_tests/test_graph.py`: Integration tests for the agent's graph.
*   `tests/unit_tests/test_configuration.py`: Unit tests for the configuration.

# Development Conventions

*   **Code Style:** The project uses `ruff` for linting and code formatting. The configuration is in the `pyproject.toml` file.
*   **Type Hinting:** The project uses type hints, and `mypy` is listed as a dev dependency, suggesting that type checking is used.
*   **Prompts:** The system prompt is defined in `src/react_agent/prompts.py`.
*   **Tools:** The tools available to the agent are defined in `src/react_agent/tools.py`.
*   **Graph:** The agent's graph is defined in `src/react_agent/graph.py`.

# Original Project Setup from Template

*   `uv add "langgraph-cli[inmem]"`: Install the langgraph CLI.
*   `langgraph new src/langgraph-app`: Create a new langgraph app.