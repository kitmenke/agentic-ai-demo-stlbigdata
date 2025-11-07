# STL Big Data Meetup: Let's Build an AI Agent

## Overview

This document outlines the plan for a hands-on session at the STL Big Data Meetup. We'll build an AI agent that can answer questions about a database.

## Agenda

1.  **Introduction to AI Agents**
    *   What is an AI Agent?
    *   Key Concepts:
        *   **Model:** The large language model (LLM) that powers the agent's reasoning.
        *   **Agent:** The autonomous entity that perceives its environment and acts to achieve its goals.
        *   **ReAct:** A framework for agents to Reason and Act.

2.  **Getting Started: The Toolkit**
    *   **uv:** A fast Python package installer.
    *   **LangChain/LangGraph:** Frameworks for building applications with LLMs.
    *   **DuckDB:** An in-process SQL OLAP database.

3.  **Live Hacking: Building a Prototype**
    *   Setting up the development environment.
    *   Defining the agent's tools for interacting with the database.
    *   Creating the agent's graph using LangGraph.
    *   Testing the agent with natural language queries.

4.  **Q&A and Next Steps**
    *   Open discussion and questions.
    *   Resources for further learning.

## Detailed Outline

### 1. Introduction to Models (No Agent)

*   **Concept:** Introduce the concept of a Large Language Model (LLM) as a powerful text-generation engine.
*   **Demo:**
    *   Create a simple Python script (`demo1_model.py`) that directly calls an LLM (e.g., OpenAI's GPT-3.5 or Anthropic's Claude).
    *   The script will include a hard-coded system prompt that provides a database schema.
    *   The user will provide a natural language question (e.g., "How many customers are in the database?").
    *   The model will generate a SQL query based on the schema and question.
    *   **Important:** The query will *not* be executed. This demo focuses solely on the model's ability to generate code.

### 2. Introduction to Tools

*   **Concept:** Introduce the concept of tools as a way for a large language model to interact with its environment.
*   **Demo:**
    *   Create a new script (`demo2_tools.py`) that demonstrates how a model can use tools to interact with a database.
    *   The script defines a set of tools: `list_duckdb_tables`, `get_table_schema`, and `query_duckdb`.
    *   The script shows a manual, step-by-step loop where the model is invoked, decides which tool to call, and the script executes the tool.
    *   This demo focuses on the tool-calling capabilities of the model, which is a foundational concept for building agents.

### 3. Building a RAG Agent

*   **Concept:** Introduce the concept of Retrieval-Augmented Generation (RAG) as a way to provide an agent with external knowledge.
*   **Demo:**
    *   This demo is split into three parts, showing how to build and use a RAG system to answer questions about DuckDB documentation.
    *   `demo3_indexer.py`: A script that reads a markdown file containing DuckDB documentation, splits it into chunks, and indexes it into a Chroma vector store using OpenAI embeddings. This creates the knowledge base for the agent.
    *   `demo3_query.py`: A script that shows how to perform a direct similarity search against the vector store to find relevant documentation for a given query.
    *   `demo3_agent.py`: A script that creates an agent with a single tool: `search_duckdb_documentation`. This tool performs a similarity search in the vector store and returns the results to the agent. The agent then uses this retrieved information to answer the user's question.

### 4. Building a LangGraph Application

*   **Concept:** Introduce LangGraph as a framework for building complex, stateful agentic applications.
*   **Demo:**
    *   Refactor the agent from the previous demo into a LangGraph application.
    *   The application will be structured as a state machine, with nodes for calling the model, executing tools, and handling the results.
    *   This demo will show how to build a more robust and maintainable agent using LangGraph.

## Demos

### Demo 1

```
cd src/demo1
uv run demo1_model.py
```

### Demo 2

```
cd src/demo2
uv run demo2_tools.py
```

### Demo 3

First download the DuckDB [offline documentation](https://duckdb.org/docs/stable/guides/offline-copy).

Then, run the indexer:
```
cd src/demo3
uv run demo3_indexer.py
```

This creates the vector store containing the indexed DuckDB documentation. Run the query program to test:
```
uv run demo3_query.py
```

Then you can run the agent:
```
uv run demo3_agent.py
```

### ReAct Agent Demo

TODO: integrate RAG into the agent

Putting it all together by running the agent:
```
uv run langgraph dev
```

Or you can chat with the agent using the existing UI: https://agentchat.vercel.app/

The movies database I created using https://www.kaggle.com/datasets/tmdb/tmdb-movie-metadata/data

## Original Project Setup from Template

*   `uv add "langgraph-cli[inmem]"`: Install the langgraph CLI.
*   `langgraph new src/langgraph-app`: Create a new langgraph app.
*   

This repository contains a Python-based ReAct agent built with the LangGraph framework, designed to interact with a DuckDB database. It allows users to query the database using natural language, leveraging a large language model to generate and execute SQL queries.