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
        *   **Model Context Protocol (MCP):** An [open-source standard](https://modelcontextprotocol.io/docs/getting-started/intro) for connecting AI applications to external systems.

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

### 2. Introduction to Agents and Tools

*   **Concept:** Introduce the concept of an AI agent as a system that can reason and act to achieve a goal. Explain that agents use "tools" to interact with their environment.
*   **Demo:**
    *   Create a new script (`demo2_agent.py`) that introduces a simple agent.
    *   The agent will have one tool: a `query_database` tool that can execute a SQL query against the DuckDB database.
    *   The agent will take a user's question, use the model to generate a SQL query, and then use the `query_database` tool to execute the query and get the result.
    *   This demo will show the basic ReAct (Reason, Act) loop in action.

### 3. Expanding the Agent's Capabilities

*   **Concept:** Discuss how to make agents more robust by giving them more tools and improving their reasoning process.
*   **Demo:**
    *   Create a new script (`demo3_multifunction_agent.py`) that enhances the agent from the previous demo.
    *   Add more tools to the agent's toolkit:
        *   `list_tables`: To see what tables are in the database.
        *   `get_table_schema`: To understand the structure of a specific table.
    *   The agent will now be able to explore the database to answer more complex questions (e.g., "What are the most popular products?").
    *   This demo will showcase a more sophisticated agent that can perform a sequence of actions to answer a question.

### 4. Building a LangGraph Application

*   **Concept:** Introduce LangGraph as a framework for building complex, stateful agentic applications.
*   **Demo:**
    *   Refactor the agent from the previous demo into a LangGraph application.
    *   The application will be structured as a state machine, with nodes for calling the model, executing tools, and handling the results.
    *   This demo will show how to build a more robust and maintainable agent using LangGraph.

## Demo

Run the agent:
```
uv run langgraph dev --no-browser
```

Chat with the agent using the existing UI: https://agentchat.vercel.app/
