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

## Outline

## Demo

Run the agent:
```
uv run langgraph dev --no-browser
```

Chat with the agent using the existing UI: https://agentchat.vercel.app/
