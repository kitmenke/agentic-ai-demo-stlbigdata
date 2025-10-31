"""This module provides example tools for web scraping and search functionality.

It includes a basic Tavily search function (as an example)

These tools are intended as free examples to get started. For production use,
consider implementing more robust and specialized tools tailored to your needs.
"""

from typing import Any, Callable, List, Optional, cast

# from langchain_tavily import TavilySearch
# from langgraph.runtime import get_runtime

# from react_agent.context import Context

import duckdb
from typing import List

db = duckdb.connect("/Users/Kit/Code/langgraph-app/database.duckdb", read_only=True)

def list_duckdb_tables() -> List[str]:
    """List all tables in the duckdb database."""
    result = db.execute("show tables").fetchall()
    return [row[0] for row in result]

def get_table_schema(table_name: str) -> str:
    """Get the schema of a table in the duckdb database."""
    result = db.execute(f"describe {table_name}").fetchall()
    schema = "\n".join([f"{row[0]} {row[1]}" for row in result])
    return schema

def query_duckdb(query: str) -> List[str]:
    """Query the duckdb database."""
    result = db.execute(query).fetchall()
    return str(result)


TOOLS: List[Callable[..., Any]] = [list_duckdb_tables, get_table_schema, query_duckdb]
