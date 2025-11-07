"""This module provides tools to interact with a DuckDB database.

The tools include:
- Listing all tables in the database.
- Getting the schema of a specific table.
- Querying the database with a custom SQL query.
"""

import os
from dotenv import load_dotenv
from langchain.tools import tool
from langchain_openai import OpenAIEmbeddings
from langchain_chroma import Chroma
from typing import Any, Callable, List
import duckdb

load_dotenv()

DATA_DIR = os.getenv("DATA_DIR")

db = duckdb.connect(f"{DATA_DIR}/movies.duckdb", read_only=True)

@tool
def list_duckdb_tables() -> List[str]:
    """List all tables in the duckdb database."""
    result = db.execute("show tables").fetchall()
    return [row[0] for row in result]

@tool
def get_table_schema(table_name: str) -> str:
    """Get the schema of a table in the duckdb database."""
    result = db.execute(f"describe {table_name}").fetchall()
    schema = "\n".join([f"{row[0]} {row[1]}" for row in result])
    return schema

@tool
def query_duckdb(query: str) -> List[str]:
    """Query the duckdb database."""
    result = db.execute(query).fetchall()
    return str(result)

# RAG demo
# https://docs.langchain.com/oss/python/langchain/rag
# Initialize the vector store
embeddings = OpenAIEmbeddings(model="text-embedding-3-large")
vector_store = Chroma(
    collection_name="demo3_duckdb_docs",
    embedding_function=embeddings,
    persist_directory=f"{DATA_DIR}/chroma_langchain_db",  # Where to save data locally, remove if not necessary
)

@tool(response_format="content_and_artifact")
def search_duckdb_documentation(query: str):
    """Search the DuckDB documentation and guides."""
    retrieved_docs = vector_store.similarity_search(query, k=2)
    serialized = "\n\n".join(
        (f"Source: {doc.metadata}\nContent: {doc.page_content}")
        for doc in retrieved_docs
    )
    return serialized, retrieved_docs

TOOLS: List[Callable[..., Any]] = [search_duckdb_documentation, list_duckdb_tables, get_table_schema, query_duckdb]
