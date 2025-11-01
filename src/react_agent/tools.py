"""This module provides tools to interact with a DuckDB database.

The tools include:
- Listing all tables in the database.
- Getting the schema of a specific table.
- Querying the database with a custom SQL query.
"""

from typing import Any, Callable, List

import duckdb

db = duckdb.connect("/Users/Kit/Data/movies.duckdb", read_only=True)

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
